FROM centos

# configure the user with password, home directory, and ssh
RUN useradd remote_user && \
    echo "remote_user:1234" | chpasswd && \
    mkdir /home/remote_user/.ssh && \
    chmod 700 /home/remote_user/.ssh

# copy the public key to the user's authorized_keys file
COPY remote-key.pub /home/remote_user/.ssh/authorized_keys

# allow the user to ssh in without a password
RUN chown -R remote_user:remote_user /home/remote_user/.ssh && \
    chmod -R 600 /home/remote_user/.ssh/authorized_keys

# generating some ssh keys for the user
RUN /usr/sbin/sshd-keygen

# start the ssh daemon
CMD /usr/sbin/sshd -D