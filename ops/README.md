# 4 Linux
Some useful linux commands to see resources:
* `uptime`: Shows how long the system has been running.
* `free`: Shows how much memory is free and how much is used.
* `df -h`: Shows how much disk space is free and how much is used.
* `less /proc/cpuinfo`: Shows the number of CPUs and their speed.
* `less /proc/meminfo`: Shows the amount of memory installed.
* `less /proc/net/dev`: Shows the network interfaces and their status.
* `less /proc/net/wireless`: Shows the wireless network interfaces and their status.
* `less /proc/net/arp`: Shows the ARP table.
* `lscpu`: CPU architecture information from sysfs and /proc/cpuinfo.
* `lsusb`: USB devices connected to the system.
* `lsblk`: Block devices connected to the system.
* `lspci`: PCI devices connected to the system.
* `lshw -C <device e.g. cpu, memory>`: List hardware information.
* `sudo dmidecode -t <device e.g. cpu, memory>`: Its a tool for retrieving hardware information of any Linux system. It dumps a computer’s DMI (a.k.a SMBIOS) table contents in a human-readable format for easy retrieval.
* `nproc`: Shows the number of processors.
* `hwinfo`: Shows the hardware information.
* `xargs`: Some of the commands in linux/unix does not accept piped input `xargs` can take the output(piped output) from one command and send it to another command as parameters.


### 4.1 File Types:
In linux everything is a file. There are multiple types of files.
* `ls -l`: Lists the files in the current directory using a long listing format. Such as `-rw-r--r-- 1 user group 1234 1234 filename`, `drwxrwxrwx 1 user group 1234 1234 filename`.
* `file name_file`: Shows the type of the file.

* `-`: Single hypen in the start indicates whether the given file is a normal file (e.g. text, ASCII file) or its a binary file (e.g. executable file).
* `d`: D in the start indicates that the type of file is directory.
* `c`: C in the start indicates that the type of file is character device. Such as keyboard, mouse, tty. These files are often found in `/dev` directory.
* `b`: B in the start indicates that the type of file is block device. Such as hard disk, floppy disk, CD-ROM.
* `p`: P in the start indicates that the type of file is pipe. A special file that allows proceses to communicate with each other without using network socket semantics.
* `s`: S in the start indicates that the type of file is socket. A special file that provides inter-process networking protected by the file system's access control.
* `l`: L in the start indicates that the type of file is symbolic link.
* `u`: U in the start indicates that the type of file is unknown.
* `w`: W in the start indicates that the type of file is a named pipe (fifo).

* `ln -s`: Creates a symbolic link.

### 4.2 Filters:
We can use `grep` to filter the files. 
* `grep keyword_search filename`: Searches the file for the keyword. If the keyword is found, the lines containing the keyword are printed.
* `grep -i keyword_search filename`: Searches the file for the keyword ignoring the case. If the keyword is found, the lines containing the keyword are printed.
* `grep keyword_search *`: Searches all the files in the current directory. 
* `grep -R keyword_search directory`: Searches all the files in the directory and subdirectories.
* `grep -v keyword_search filename`: Displays the lines in the file that do not contain the keyword. It is called reverse search.


* `less filename`: Displays the file in the terminal. It is a filereader. Less is very good for reading large files because with large input files it starts up faster than text editors like vi/vim. To navigate the file, we can use arrow keys or vim navigation keys.
* `more filename`: More is a similar utility to less. It is a file reader. It is similar to less but it displays the file in the terminal in pages. To navigate the file, we can user arrow keys to navigate.
* `head filename`: Displays the first 10 lines of the file. We can change the number of lines displayed by using `-n` option.
* `tail filename`: Displays the last 10 lines of the file. We can change the number of lines displayed by using `-n` option. We can also use `-f` option to read the file dynamically. It is very convenient when we are reading logs.
* `cat filename`: Concatenate files and print on the standard output.
* `cut -d<delimeter e.g. comma, colon etc> -f<number of the column e.g. 1, 2, 3> filename`: Remove sections from each line of files. Example use case would be to see the column of a csv file as `cut -d, f1 file.csv`.
* `awk '{print $1}' filename`: Prints the first column of the file. Awk is a pattern scanning and processing language that can be used to perform simple text file manipulation. Awk is specialized for textual data manipulation.
* `sed 's/<old_string>/<new_string>/g' filename`: Replaces the old string with the new string and prints to the standard output. The `g` option is used to replace all occurrences of the old string. If we want to write changes to the file we need to specify the `-i` flag. But it is a good practice to first see the changes and then save them.

### 4.3 Redirection:
* We can redirect the output of a command to a file by using `>` operator. Example: `ls -l > file.txt`. A single `>` operator overwrite the file while a double `>>` operator appends the file. By default, `>` operator is equivalent to `>&1`, which means redirecting the output to the file.
* But if we want to redirect the error to a file, we can use `2>` operator. Example: `ls -l 2> file.txt`. The `2>` operator redirects the error to the file. 
* Another option to redirect anything i.e. output/error to the file we can use `&>` operator. Example: `ls -l &> file.txt`.
* To clear the content of a file we can use `cat /dev/null > file.txt`. This will wipe out all the content of that particular file.
* `wc`: Counts the number of lines, words, characters and byte in a file. To count lines we can do `wc -l filename`.
* `find`: Search for files in a directory hierarchy. Example: `find . -name "*.txt"`. Find is a real-time search tool.
* `locate`: The locate command is a Unix utility used for quickly finding files and directories. The command is a more convenient and efficient alternative to the find command, which is more aggressive and takes longer to complete the search. Opposite to find, the locate command doesn't search the entire filesystem, but looks through a regularly updated file database in the system. It is not preinstalled on most systems. We can install it using `mlocate` e.g. `sudo apt-get install mlocate`. We can update its database using `updatedb`.

### 4.4 Users and Groups:
Every file in the system is owned by a user and an associated group with it. We can control the how much permissions/authorization a user has to a file. Every user has an id called `UID`. All the username and UID information is stored in the `/etc/passwd` file. Users password and other encrypted information is stored in the `/etc/shadow` file. Users are assigned a `home` directory and a program that is run when they login which is usually `shell`.

<!-- table of 4 rows and 6 columns -->
|Type    |Example         |User ID      |Group ID     |Home Dir      |Shell        |
|--------|--------        |--------     |--------     |--------      |--------     |
|Root    |root            |0            |0            |/root         |/bin/bash    |
|Regular |danish          |1000 to 60000|1000 to 60000|/home/username|/bin/bash    |
|Service |ftp, ssh, apache|1 to 999     |1 to 999     |/var/ftp etc  |/sbin/nologin|

* `whoami`: Prints the name of the user.
* The format of the `/etc/passwd` file is: `username:password:UID:GID:Full Name:Home Directory:Shell`.
* The `/etc/group` file contains the group name and the group ID. The format of the file is: `groupname:groupID:user1,user2,user3`.
* The `id user` command prints the user ID and the group ID and some other information.
* The `useradd usename` command creates a new user account using the values specified on the command line plus the default values from the system. We can't login to these users without creating a password for them. 
* If we are using `ubuntu`, then `useradd` will not work properly it will not create `home` directory etc. To avoid that problem we can use `adduser` command to create a new user.
* The `groupadd groupname` command creates a new group account using the values specified on the command line plus the default values from the system The new group will be entered into the system files as needed.
* The `usermod` command modifies the system account files to reflect the changes that are specified on the command line. Example: `usermod -aG groupid/groupname userid/username`.
* `passwd username`: Changes the password of the user.
* `last`: Displays the last logged in users.
* `lsof`: Displays the files that are open by the user. Example: `lsof -u username`. If the utility is not installed, it will be installed using `sudo apt-get install lsof`, `sudo yum install lsof`, or whatever your package manager is.
* `userdel`: Deletes a user account. Example: `userdel username`. To delete the user's home directory, we can use `usedel -r username`.
* `groupdel`: Deletes a group account. Example: `groupdel groupname`.
* `su - username`: Logs in as the specified user. We can use this command to switch between different users.

### 4.5 File Permissions:
File permissions can be viewed by using `ls -l` command. The `ls` command is an example of read, `cd` command is an example of executable, and `rm` command is an example of write permission.
```shell
$ ls -l /bin/login
-rwxr-xr-x 1 root root 38840 مارچ   28 17:34 /bin/login
```
* The format of above output is: `permissions user/owner group size month day time filename`.
* `-rwx` means that the root user have the permissions to read, write and execute the file.
* `r-x` means read and execute permissions for the root group.
* `r-x` means read and execute permissions for the other users.
* This completes `-rwxr-xr-x` which means that the file is readable, writable and executable by the root user, readable and executable by the root group and finally readable and executable by the other users.
* The permissions string of any file consist of 10 characters/bits i.e. `---------`. As a group of 4 `(-)(---)(---)(---)` -> `(type)(user permissions)(group permissions)(others permissions)`.
* `-`: The first character/first group represents the file type.
* `---`: The second three characters/second group represent the file permissions for the mentioned user.
* `---`: The third three characters/third group represent the file permissions for the mentioned group.
* `---`: The fourth three characters/fourth group represent the file permissions for the other users.
* Permissions are of three types: `r` for read, `w` for write, and `x` for execute.


* `chown` command changes the ownership of a file. Example: `chown username filename/directory`. This command changes the ownership of the file to the user with the specified username. To change the owner and group as well, we can do: `chown username:groupname filename/directory`. To change the ownership of all the files in the directory, we can add `-R` flag to the command.
* `chmod` command changes the file mode bits of each given file according to mode, which can be either a symbolic representation of changes to make, or an octal number representin the bit pattern for the new mode bits. A combination of the  letters `ugoa` controls which users access to the file will be changed. Instead of one or more of these letters, you can specify exactly one of the letters `ugo` here `u` is user, `g` is group and `o` is others. The `+` means add the permission and `-` means remove the permission. An example of the command is: `chmod u+x filename`, which adds the executable permission to the file for the. This `chmod o-w` command removes the write permission for the other users.
* We can also change permissions numerically using the octal number. Example: `chmod 755 filename`. In the number `755`, first digit represents the user permissions, second digit represents the group permissions and third digit represents the other users permissions. The number `4` is for read, `2` for write and `1` for execute, and their sum can be used to determine permissions. So in `755` the user has read, write and execute permissions, because if we sum `4`, `2` and `1` we'll get `7`. Similarly the second digit `5` indicates the group has read and execute permissions and finally the third digit `5` indicates the other users have read and execute permissions. If we have `0` in any position that means no position is allowed.


### 4.6 Sudo
The `sudoers` file is a file Linux and Unix administrators use to allocate system rights to system users. This allows the administrator to control who does what.  When you want to run a command that requires root rights, Linux checks your username against the sudoers file. Linux checks the username against the sudoers file. This happens when we type the command “sudo”. If it determines, that our username is not on the list, you cannot run the command/program logged in as that user. The file can be found as `vi /etc/sudoers`. The permissions of the file are as follows:
```shell
$ ls -l /etc/sudoers
-r--r-----. 1 root root 4328 Feb 12 17:54 /etc/sudoers
```
The permissions of the file is read only for root and the root group, no write permissions. The `visudo` command opens the sudoers file and only then we can write to the sudoers file.
```shell
## Allow root to run any commands anywhere
root        ALL=(ALL)       ALL
```
We can search for the above line or `root` in the `sudoers` file, and then below that line we can add another user whom we want to grant `sudo` access. For example:
```shell
## Allow root to run any commands anywhere
root        ALL=(ALL)       ALL
aws        ALL=(ALL)       ALL
```
If want that the user shouldn't be asked password when executing commands as `sudo`, then we can add `NOPASSWD: ` before the last `ALL`. Example below:
```shell
## Allow root to run any commands anywhere
root        ALL=(ALL)       ALL
aws        ALL=(ALL)       NOPASSWD: ALL
```

Editing the `sudoers` file is not safe, because if we make a syntax error the `sudoers` file will not be functional and all the `root` privalges won't work. In that case we will not be able to edit/change the `sudoers` file if a password is not set for root user, which in most servers is not set. 

So a better solution is instead of editing the `sudoers` file we can create a `sudoers` like file in `/etc/sudoers.d` directory having the same name as user/group, and we can add the following line to that file.

For example we want to grant `sudo/root` access to `aws` user for that we will add the following line to the `/etc/sudoers.d/aws` file. 

```shell
aws        ALL=(ALL)       NOPASSWD: ALL
```

And if we want want to grant `sudo/root` access to `devops` group for that we will add the following line to the `/etc/sudoers.d/devops` file. 

```shell
%devops        ALL=(ALL)       NOPASSWD: ALL
```
Here the sign `%` indicates that its a group.

### 4.7 Processes:
* `Zombie Process`: A process that is not running anymore, but is still in the process table.
* `Orphan Process`: A process whose parent process is not running anymore.
* `ps aux`: This command lists all the processes running in the system to standard output.
* `ps`: This command displays the processes running on the system.
* `ps -ef`: This command check all the processes with thier parent process id.
* `kill process_id`: This command kills the process and all its child processes gracefully.
* `kill -9 process_id`: This command kills the process and all its child processes forcefully.
  
Let's say we want to find all the process of a particular programs such as `httpd`. We can use the following command:
```shell
$ ps -ef | grep httpd | grep -v grep
```
To kill all of httpd processes forcefully we can use the following command:
```shell
$ ps -ef | grep httpd | grep -v grep | awk '{print $2}' | xargs kill -9
```
This will filter the `httpd` process then using `awk` it will filter the second column which contains `process ids` and then using `xargs` to feed the `process ids` to `kill` it will kill all the processes.

### 4.8 Archiving and Compression:
* `tar`: This command archives a file or a directory. Different flags are used to archive/unarchive a file or a directory. The `tar` file is often known as `tar ball`.
* `A`: Append archive to the end of another archive.
* `c`: Create an archive.
* `d`: Find differences between archives and filesystem.
* `f filename`: The name of the archive file.
* `r`: Append files to the end of an archive.
* `t`: Table of contents: tell me what's in an archive.
* `u`: Append files which are newer than the corresponding copy in the archive.
* `v`: Verbose: tell me what's going on.
* `x`: Extract from an archive.
* `z`: Put the archive through gzip. gzip/gunzip is a GNU compression utility.

We can use any combination of the above flags to create or unzip an archive. For example:
```shell
$ tar -czvf my_archive.tar my_file.txt
```
The above command creates the tar archive `c` for create, `z` for gzip compress and `v` for verbose and `f` for filename.

* An alternative way for archiving is to use the `zip` and `unzip` utilities. But these utilities are not available on all Linux distributions, we need to install them.