# 1. Ansible

### 1.1. Ansible Inventory
* Ansible is agentless automation tool that can be used to manage infrastructure. 
* Agentless automation is a way to automate infrastructure without any agent i.e. we don't need to install any agent (Ansible) on the infrastructure i.e. target machines to perform the automation.
* In case of linux Ansible make use of SSH for communication between the infrastructure and the Ansible server.
* In case of Windows Ansible uses PowerShell Remoting to communicate between the infrastructure and the Ansible server.
* Information about target systems is stored in `inventory` file, which is written in `ini` format.
* In case of Ansible, inventory file is stored in `/etc/ansible/hosts` file by default.
* Inventory file contains information about the target systems (servers) like IP address, username, password, port number etc. As show below

```ini
Server1.company.com
Server2.company.com
```

* We can group multiple target systems(servers) together i.e. as follows

```ini
Server1.company.com
Server2.company.com

[web]
Server3.company.com
Server4.company.com

[db]
Server5.company.com
Server6.company.com

[mail]
Server7.company.com
Server8.company.com
```

* We can also group, groups of servers together for that we need provide name of the group following by colon and the keyword `children` 

```ini
Server1.company.com
Server2.company.com

[web]
Server3.company.com
Server4.company.com

[db]
Server5.company.com
Server6.company.com

[mail]
Server7.company.com
Server8.company.com

[all:children]
web
db
mail
```
* We can also provide alias to the servers, by providing alias(i.e the name you want to give to the server), and the assigning the address of the server to `ansible_host` parameter. An example is given below:

```
web ansible_host=Server3.company.com
db ansible_host=Server5.company.com
mail ansible_host=Server7.company.com
```
* The `ansible_host` is an inventory parameter used to specify the FQDN or IP address of the server.
* There are other inventory parameters to such as:
  - `ansible_connection`: This parameter is used to specify the connection type to the server e.g. `ssh`, `winrm`, `localhost` etc.
  - `ansible_port`: This parameter is used to specify the port number of the server e.g. `22`, `5986` etc.
  - `ansible_user`: This parameter is used to specify the username to connect to the server e.g. `root`, `administrator` etc.
  - `ansible_ssh_pass`: This parameter is used to specify the password to connect to the server. But a better practice is to use Ansible Vault to store the password in encrypted form.
* An example of inventory file is given below:

```ini
web ansible_host=Server1.company.com ansible_connection=ssh ansible_user=root
db ansible_host=Server2.company.com ansible_connection=winrm  
mail ansible_host=Server3.company.com ansible_connection=ssh

localhost ansible_connection=local
``` 

### 1.2. Ansible Target Machine Ping:
* We can connect to a ansible target machine by providing its `IP Address`.
* We can check `IP Address` of our target machine using `ip addr` command.
* Then we can use `ssh <ip_addr>` command and provide password to connect to the target machine which. The password for Vagrant VMs are `vagrant`.
* We can also define ansible inventory file to add our targets as follows and save in `inventory.txt`
  
```ini
target1 ansible_host=192.168.56.80 ansible_ssh_pass=vagrant
```

* Then we can use following command to ping our server/target.

```bash
ansible target1 -m ping -i inventory.txt
```

* If `ssh fingerprint` error occurs then we need to `ssh` to the target machine manually and accept the fingerprint of the target machine e.g.

```bash
ssh <ipv-address-of-target>
```

### 1.3. Ansible Playbooks:
* `Playbook` is a single YAML file containing plays.
* A `Play` defines set of activities or task to be run on hosts.
* A `Task` is a single action to be performed on a host e.g. 
  - installing a package.
  - copying a file etc.
* A sample `Ansible Playbook` is given below:

```yaml
name: Play 1
hosts: localhost
tasks:
  - name: Task 1
    command: echo "Hello World"
  
  - name: Install httpd service
    yum:
      name: httpd
      state: present
  - name: Start httpd service
    service:
      name: httpd
      state: started
``` 

* The `name` parameter is used to provide name to the play.
* The `hosts` parameter is used to provide the target hosts on which the play will be executed. The hosts should be defined in the inventory file.
* Tasks are the actual tasks to be performed on the target hosts. The tasks are defined under `tasks` parameter.
* We can choose a single host, multiple host or group of hosts from the inventory file to run the play.
* `Ansible Modules:` The different actions run by tasks are called modules e.g. `command`, `yum`, `service` etc. are the modules. 
* Ansible modules are reusable, standalone scripts that can be used by the Ansible API, or by the ansible or ansible-playbook programs.
* They return information to ansible by printing a JSON string to stdout before exiting. 
* We can also use `ansible-doc` command to get the documentation of the module e.g. `ansible-doc yum` will give the documentation of `yum` module.
* To get the list of already available modules we can use `ansible-doc -l` command.
* We can run a ansible playbook by following command:

```bash
ansible-playbook playbook.yml
```

* There are two ways of running commands on target machines either by using imperative approach or declarative approach.
* In imperative approach we directly specify the commands to be run on the target machines e.g. as follows:

```bash
ansible all -m ping -i inventory.txt
```

* In the above command `all` is the group of hosts on which the command will be run. The `-m` parameter is used to specify the module to be used and `-i` parameter is used to specify the inventory file.
* In declarative approach we use `playbook` to specify the tasks to be run on the target machines:

```yaml
-
  name: Test connectivity to the target servers
  hosts: all
  tasks:
    - name: Ping Test
      ping:
```

### 1.4. Ansible Modules:
* Ansible modules are categorized into groups based on their functionality.
* `System Modules:` are actions to be performed at system level such as modifying the Users, Groups on the system, modifying the IP Tables and Firewall rules, modifying the SELinux policies etc, some of them are listed below:
  - User
  - Group
  - Hostname
  - Iptables
  - Lvg
  - Lvol
  - Make
  - Mount
  - Ping
  - Timezone
  - Systemd
  - Service

* `Command Modules:` are used to execute simple commands on target machines, some of them are listed below:
  - Command: Execute a simple command
  - Expect: Execute a command expecting a prompt i.e interactively
  - Shell: Execute a command in a shell
  - Script: Run a script on the target machine
  - Raw: Execute a command without going through the Ansible module system

* `File Modules:` help in working with files such as using `Acl` module to set and retrieve `Access Control List` of a file. Some of the file modules are listed below:
  - Acl
  - Copy
  - File
  - Lineinfile
  - Mount
  - Replace
  - Stat
  - Template
  - Unarchive

* `Database Modules` help in working with databases such as `MongoDB`, `PostgreSQL` etc. To add and remove databases or modifying database configurations.
  
* `Cloud Modules` help in working with cloud services such as `AWS`, `Azure`, `GCP` etc. To create and delete cloud resources, performing configuration changes, networking, security, managing containers, data centres, clusters virtual machines etc. Some of the Cloud modules are listed below:
  - AWS
  - Azure
  - GCP
  - Digital Ocean
  - Docker
  - Linode
  - Openstack
  - Cloudstack
  - VMware
  - Cloudscale
  - Smartos

* `Windows Modules:` help working with MS Windows Environment.
* There are a lot of other modules available in Ansible which can be used to perform different tasks on target machines. The list can be found in the [documentation](https://docs.ansible.com/ansible/2.9/modules/list_of_all_modules.html)

### 1.5. Command Module:
* The [command](https://docs.ansible.com/ansible/2.9/modules/command_module.html) module is used to execute a command on the target machine.
* The command module takes the command name followed by a list of space-delimited arguments.
*  The `chdir` parameter change into the given directory before executing the command.
*  The `creates` can be used with `mkdir` as `mkdir /folder creates=/folder` it will only create a folder only if it does not exist.
*  The parameter `free_form` indicates that `command` module takes free form input, instead parameterized input i.e. all the arguments and parameters to the command are passed in the same line.
*  `copy` command uses parameterized input i.e. `src` and `dest`.
*  An example of playbook using command is given below:

```yaml
-
  name: Play1
  hosts: localhost
  tasks: 
    - name: Execute command date
      command: date
    
    - name: Display resolv.conf contents
      command: cat /etc/resolv.conf

    - name: Display resolv.conf contents
      command: cat resolv.conf chdir=/etc
    
    - name: Create a folder
      command: mkdir /folder creates=/folder
    
    - name: Copy file
      command:
        cmd: cp /etc/resolv.conf /etc/resolv.conf.bak
        creates: /etc/resolv.conf.bak
```

### 1.6. Script Module
* The [script](https://docs.ansible.com/ansible/2.9/modules/script_module.html) module is used to execute a script on the target machine or node.
* It runs a local script on a remote node after transferring it, we don't need to manually copy it to the remote node.
* Following is the syntax of script module:

```yaml
-
  name: Play1
  hosts: localhost
  tasks: 
    - name: Execute script
      script: /path/to/script.sh -arg1 -arg2
```

### 1.7. Service Module:
* The service module is used to Start, Stop or Restart a service.
* A sample playbook is given to start the various services:

```yaml
-
  name: Play1
  hosts: localhost
  tasks: 
    - name: Start postgresql service
      service:
        name: postgreql
        state: started
    
    - name: Start httpd service
      service:
        name: httpd
        state: started
    
    - name: Start nginx service
      service:
        name: nginx
        state: started
```

* To start a service we need to provide the name of the service and the state to be `started`, or any other desired state such as `restarted` or `stopped`.
* We are specifying `started` because we want to ensure that the service is started, if its not already started.
* But if the service is already started then do nothing.
* This is called `idempotency` i.e. the state of the system should not change if the task is run multiple times.
* Ansible documentation states that `idempotency` as follows:
  - An operation is idempotent if the result of performing it once is exactly the same as the result of performing it repeatedly without any intervening actions.
* Majority of the modules in ansible are idempotent and ansible highly recommends this.

### 1.8. LINEINFILE Module:
* Search for a line in a file, and replace it or add it if needed.
* Let's say we want to add a new server into our `/etc/resolv.conf` file, we can do this by using the `lineinfile` module.
* The following playbook uses `lineinfile` module to add a new server to the `/etc/resolv.conf` file:

```yaml
-
  name: Play1
  hosts: localhost
  tasks: 
    - name: Add a new server to resolv.conf
      lineinfile:
        path: /etc/resolv.conf
        line: `nameserver 10.1.250.10`
```

* The `lineinfile` module is also idempotent, it will not add the line if it already exists.
* If we use the script `echo "nameserver 10.1.250.10" >> /etc/resolv.conf` to add the same line, it will add the line again and again every time we run the script which is not desired. 
* The `lineinfile` module will not add the line if it already exists, it will make sure that there is only one instance of the line in the file.