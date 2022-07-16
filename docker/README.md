# 1. Introduction to Docker and Containerization.

### 1.1 Virtual Machine vs Conainerization:
* Virtual Machines tend to be more  computationally expensive and more complex than containers.
* Virtual Machines can solve the problem handling multiple environments but they waste a lot of computational and storage resource which makes our host system very slow.
* Sharing re-building, and distribution of VMs can be challenging.
* Virtuall Machines encapsulate "whole machines" instead of just apps and environments.
* Containers are a more lightweight and easier to use than virtual machines.
* Containers are more portable and can be used on multiple platforms as sharing, re-building and distribution is easy.
* Containers Encapsulates apps/environments instead of whole machines.

# 2. Docker Building Blocks (Images and Containers).

### 2.1 Dockerfile Important Commands:
* `FROM`: This command tells Docker to build a new image from an existing image.
* `RUN`: This command runs a command in the container. We can define simple subcommands along with the RUN instruction that we want to execute inside the container. For example, if we want to install a pip package, we can simply use the “RUN pip install package_name” instruction inside the Dockerfile.
* `COPY`: This command copies files from the host to the container.
* `WORKDIR`: This command changes the current working directory in the container.
* `EXPOSE`: This command exposes a port on the host. This command exposes the specified port but it does not publish/map the container port to the host port. To do that we need to specifiy `publish` argument with `docker run` as `docker run -p host_port_number:docker_port_number` the `EXPOSE` command is optional, but its a good practice to specify it.
* `ENTRYPOINT`: This command sets the entrypoint of the container. The `ENTRYPOINT` specifies a command that will always be executed when the container starts.
* `CMD`: This command sets the command that is run when the container is started. The `CMD` specifies arguments that will be fed to the `ENTRYPOINT`.

If you want to make an image dedicated to a specific command you will use `ENTRYPOINT ["/path/dedicated_command"]`. Otherwise, if you want to make an image for general purpose, you can leave `ENTRYPOINT` unspecified and use `CMD ["/path/dedicated_command"]` as you will be able to override the setting by supplying arguments to docker run.

### 2.2 Understanding Image Layers:
Images are layer based. An Image is built up from multiple layers based on the different instructions. Every instruction create a layer. These layers are cached. 

When an image is buid/re-build only the instruction where change happed and all the instruction after that instruction are reevaluated rest of them are used from cached layers. This speeds up the image build time. In addition an image is read only. It means once an image is buit/rebuild it cannot be modified.

### 2.3 Docker run vs start:
* `docker run`: This command creates a new container based of the specified image.
* `docker start`: This command starts a container that is already created.
* If we haven't changed anything i.e. the image is not changed, then there is no need for `docker run` command. We can simply use `docker start` command. With `docker start` command, the container is run in the background. 
* The `docker stop` command does not remove the container data or the data created data while the container was running, if start the container by `docker start`, we can find the data that was previously created, we only loose data when a container is removed.
* The `docker run` command runs in attached mode while `docker start` runs in detached mode. To run a container in detached mode, we need to use the `-d` flag as `docker run -d`.
* We can attach to a detached container by running `docker attach container_id`.
* We can also use `docker logs` to see the logs of a container, and by adding `-f` flag to `docker logs` we can see the logs of a container in real time just as we are attached to the container.

### 2.4 Docker interactive mode:
To run Docker container in interactive mode we can combine `-i` and `-t` flags. For example, `docker run -it` will run the container in interactive mode and attach to it.

* `-i` flag Keep STDIN open even if not attached.
* `-t` flag Allocate a pseudo-TTY.
* If a running container is detached, we can still enter into its interactive mode by using the `docker exec -it` command.
* With `docker start` we can use `-ai` flag to start a container in interactive mode, but this will only work if the continer started in interactive mode.

### 2.5 Docker remove container images and containers:
* `docker ps`: This command lists all the containers that are running.
* `docker ps -a`: This command lists all the containers that are running and also stopped.
* `docker rm container_name/id`: This command removes a container. If the container is running, it will be stopped first.
* To delete all the conatiners we can combine the two commands as: `docker rm $(docker ps -a -q)`.
* `docker images`: This command lists all the images that are available.
* `docker rmi image_id`: This command removes an image.
* `docker rmi $(docker images -q)`: This command removes all the images.
* We can only remove those images that are not being used by any container anymore and that includes the stopped containers as well. That is why a container need to be removed first.
* If we want to remove all the image that are not being used by any containers anymore we can use `docker image prune` command.
* One better way is to remove docker containers automatically once they are stopped. We can achieve that by adding `-rm` flag to the `docker run` command as `docker run -rm image_tag/id`.

### 2.6 Inspecting a Docker image:
`docker inspect image_id`: This command is used to inspect the image. It returns a JSON object that contains the image details such as when the image was created, how many layers it has etc.

### 2.7 Copying files to and from a Docker container:
We can copy files to and from a running Docker container using the `docker cp` command.
`docker cp source_path container_id:destination_path`: This command copies a file from the host to the container.
`docker cp container_id:source_path destination_path`: This command copies a file from the container to the host.

### 2.8 Naming and tagging Docker images:
* We can give a name to docker container by providing `--name` flag to the `docker run` command as `docker run --name my-container container_name/id`.
* We can also provide a name and tag to docker image by proving `--tag` and `-t` flags to the `docker build` command as `docker build --tag my-image:1.0`. Name and optionally a tag in the 'name:tag' format.

# 3. Docker Volumes and Managing Data.
