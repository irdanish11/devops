# 1. Ansible

### 1.1 Ansible Inventory
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
