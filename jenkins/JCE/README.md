
# 4 Jenkins CI:

### 4.1 Tomcat in Staging Environment:
* Tomcat is an application web-server, it executes Java servlet and renders Web pages that include Java Server Page coding. 
* Install tomcat either using the package manager e.g. `pacman` or using `wget` and download the [zip](https://tomcat.apache.org/download-10.cgi) and install.
* If installed with `pacman` the installation will be available at `/etc/tomcat<version_number>`, version_number can be 8, 9 or 10 or something similar.
* Tomcat runs on port `8080` by default but if you want to change the port then you can do it by editing the `server.xml` file. 
* Find the `Connector` tag and change the port to `8080` to desired port and save the file.
* Add the following roles the file `tomcat-users.xml`:

```xml
  <role rolename="manager-script"/>
  <role rolename="admin-gui"/>
  <user username="tomcat" password="tomcat" roles="manager-script,admin-gui"/>
```
* Start the tomcat server by running the following command:

```bash
  sudo systemctl start tomcat
```

### 4.2 Deploy to Staging Environment:
* First we'll create a job to produce `Tomcat Deployable Artifacts`. 
* In CI section we have created artifact, and the artifact was a `jar` file.
* The `jar` file can't be deployed to `Tomcat`.
* In this section we have `Java servlet` project which creates `.war` file.
* We need to install to plugins:
    - `Copy Artifact:` The `Copy Artifact` plugin is used to copy the artifact to the specified directory.
    - `Deploy to Containers:` The `Deploy to Containers`is used to deploy the artifact to the specified container e.g. Tomcat.