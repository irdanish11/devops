# 1. Jenkins


### 1.1 Setup GitHub SSH with Jenkins:
* Open up your terminal. 
* Check if jenkins is available as a user by following command.

```shell
cat /etc/passwd | grep jenkins
```

* If jenkins is installed and setup properly, you should see the following output:

```shell
jenkins:x:957:957:Jenkins CI:/var/lib/jenkins:/usr/bin/nologin
```

* It confirms the `jenkins` user is available now login to the `jenkins` user by following command:

```shell
sudo -su jenkins
```

* Now we are logged into the Jenkins user now we need to create the SSH key for GitHub by following this [Guide](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent) or using following set of commands:

```shell
ssh-keygen -t ed25519 -C "your_email@example.com"
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519
```

* Now we need to add the public key to the SSH/GPG keys section in our GitHub's settings.
* Copy the SSH public key to your clipboard:

```shell
cat ~/.ssh/id_ed25519.pub
```

* The above command will show your public key copy and add into the SSH/GPG keys section in your GitHub's settings. 

* Now we will add the SSH credentials (i.e. private key) to our Jenkins Server.
* In the Jenkins server goto `Manage Jenkins > Manage Credentials > global > Add Credentials`.
* Now under the `Kind` drop down menu select `SSH Username with private key`.
* Add `ID` and `Description` fields whatever you want.
* Add `jenkins` to the `Username` field.
* Under the `Private Key` check `Enter directly` radio button.
* Now copy your private key to the clip board by following command:

```shell
cat ~/.ssh/id_ed25519
```

* Copy the private key starting from `-----BEGIN PRIVATE KEY-----` to `-----END PRIVATE KEY-----` and paste it into the `Private Key` field.
* Then click on create and start using it in your Jenkins  jobs.

