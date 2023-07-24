import os
import sys
import signal
import subprocess
import multiprocessing


def sigterm_handler(nginx_pid: int, gunicorn_pid: int) -> None:
    """
    Handle SIGTERM signal by killing the Nginx and gunicorn server.

    Args:
        nginx_pid: The process id (pid) of the nginx process.
        gunicorn_pid: The process id (pid) of the gunicorn process.
    """
    try:
        os.kill(nginx_pid, signal.SIGQUIT)
    except OSError:
        pass
    try:
        os.kill(gunicorn_pid, signal.SIGTERM)
    except OSError:
        pass
    sys.exit(0)


def start_server() -> None:
    """
    Starts the Gunicorn Server for Web Server Gateway Interface (WSGI) app
    behind Nginx proxy server. Gunicorn allows the app to run concurrently 
    in a production environment.
    """
    cpu_count = multiprocessing.cpu_count()
    server_timeout = os.environ.get('SERVER_TIMEOUT', 60)
    server_workers = int(os.environ.get('SERVER_WORKERS', cpu_count))
    app_dir = os.environ.get('APP_DIR', '/app') 
    print(f"App directory: {app_dir}")

    print("Linking the Nginx log streams to stdout/err so they will be logged to the container logs.")
    subprocess.check_call(['ln', '-sf', '/dev/stdout', '/var/log/nginx/access.log'])
    subprocess.check_call(['ln', '-sf', '/dev/stderr', '/var/log/nginx/error.log'])

    print(f"Starting the Gunicorn WSGI Server with {server_workers} workers.")
    nginx = subprocess.Popen(['nginx', '-c', f'/{app_dir}/nginx.conf'])
    gunicorn = subprocess.Popen(['gunicorn',
                                 '--timeout', str(server_timeout),
                                 '--worker-class', 'gevent',
                                 '--bind', 'unix:/tmp/gunicorn.sock',
                                 # '--bind', '0.0.0.0:8050',
                                 '--workers', str(server_workers),
                                 '--threads', str(server_workers * 2),
                                 'wsgi:app'])

    # Setting up the handler for unix signal terminate asynchronous event.
    signal.signal(signal.SIGTERM, lambda a, b: sigterm_handler(nginx.pid, gunicorn.pid))
    # If either subprocess exits, so do we.
    pids = set([nginx.pid, gunicorn.pid])
    while True:
        pid, status = os.wait()
        if pid in pids:
            print(f"\n\nProcess {pid} exited with status {status}\n\n")
            break

    sigterm_handler(nginx.pid, gunicorn.pid)
    print('Server exiting...')


if __name__ == '__main__':
    start_server()
