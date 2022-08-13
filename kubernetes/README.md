
# 1. Introduction to Kubernetes

### 1.1 What is Kubernetes?
* Kubernetes is a portable, extensible, open source platform for managing containerized workloads and services, that facilitates both declarative configuration and automation. 

<p align="center">
<img src="images/container_evolution.svg">
</p>

* ***Traditional deployment era:*** Early on, organizations ran applications on physical servers. There was no way to define resource boundaries for applications in a physical server, and this caused resource allocation issues. 
* ***Virtualized deployment era:*** As a solution, virtualization was introduced. It allows us to run multiple Virtual Machines (VMs) on a single physical server's CPU. 
* ***Container deployment era:*** Containers are similar to VMs, but they have relaxed isolation properties to share the Operating System (OS) among the applications. Therefore, containers are considered lightweight. 
* Containers are a good way to bundle and run our applications. In a production environment.
* We need to manage the containers that run the applications and ensure that there is no downtime.
* For example, if a container goes down, another container needs to start. Wouldn't it be easier if this behavior was handled by a system?
* That's how Kubernetes comes to the rescue! Kubernetes provides us with a framework to run distributed systems resiliently. 
* It takes care of scaling and failover for our application, provides deployment patterns, and more. For example, Kubernetes can easily manage a canary deployment for our system.
* Kubernetes provides us with:
    - **Service discovery and load balancing** Kubernetes can expose a container using the DNS name or using their own IP address. If traffic to a container is high, Kubernetes is able to load balance and distribute the network traffic so that the deployment is stable.
    - **Storage orchestration** Kubernetes allows us to automatically mount a storage system of our choice, such as local storages, public cloud providers, and more.
    - **Automated rollouts and rollbacks** us can describe the desired state for our deployed containers using Kubernetes, and it can change the actual state to the desired state at a controlled rate. For example, us can automate Kubernetes to create new containers for our deployment, remove existing containers and adopt all their resources to the new container.
    - **Automatic bin packing** us provide Kubernetes with a cluster of nodes that it can use to run containerized tasks. us tell Kubernetes how much CPU and memory (RAM) each container needs. Kubernetes can fit containers onto our nodes to make the best use of our resources.
    - **Self-healing** Kubernetes restarts containers that fail, replaces containers, kills containers that don't respond to our user-defined health check, and doesn't advertise them to clients until they are ready to serve.
    - **Secret and configuration management** Kubernetes lets us store and manage sensitive information, such as passwords, OAuth tokens, and SSH keys. us can deploy and update secrets and application configuration without rebuilding our container images, and without exposing secrets in our stack configuration.

### 1.2 Why Kubernetes? Amazon ECS vs Kubernetes:
* ***ECS:***
  - Amazon ECS is a proprietary solution that leverages Amazon’s EC2 and Fargate platforms to host Docker containers providing serverless computing, on-demand pricing, scalability, security, reliability, and cost-efficiency.
  - ECS is cloud dependent and only offered by AWS.
  - Initial setup and deployment is very easy on ECS
  - ECS allows up to 120 tasks per instance.
  -  ECS is a proprietary managed service, it offers little in terms of configuration. This is even more true if we use the Fargate platform, as there is no access to cluster nodes, which restrict troubleshooting altogether. 
* ***Kubernetes:***
  - Kubernetes is on the other hand, is an open-source container orchestration solution that can be hosted on many platforms, and offers a lot more flexibility in terms of configuration and non-standard applications. 
  - Kubernetes is cloud agnostic.
  - Kubernetes requires a little more expertise. If us are on EKS, us will have the benefit of setting up through the AWS Management Console, but us will still need to configure and deploy pods via Kops.
  - Kubernetes has much higher limits in general — even supporting up to 750 pods per instance on EKS. These limits may look very important at first glance, but become critical when deploying large apps that require thousands of pods and nodes.
  - Kubernetes, offers flexibility and customizability and we can access cluster nodes and pods directly.

### 1.3 Kubernetes Architecture:
* Kubernetes is a distributed system that is composed of a number of components.
* ***Pods:***
  - Pods are the smallest deployable units of computing that you can create and manage in Kubernetes.
  - A Pod is a group of one or more containers, with shared storage and network resources, and a specification for how to run the containers.
  - A Pod's contents are always co-located and co-scheduled, and run in a shared context. 
  - A Pod models an application-specific "logical host": it contains one or more application containers which are relatively tightly coupled. 
  - In non-cloud contexts, applications executed on the same physical or virtual machine are analogous to cloud applications executed on the same logical host.
  - The shared context of a Pod is a set of Linux namespaces, cgroups, and potentially other facets of isolation - the same things that isolate a Docker container.
  - In terms of Docker concepts, a Pod is similar to a group of Docker containers with shared namespaces and shared filesystem volumes

* ***Worker Node:*** 
  - A Kubernetes cluster consists of a set of worker machines, called nodes, that run containerized applications. Every cluster has at least one worker node.
  - The pod (having a container or multiple containers inside of it) runs on a worker node. 
  - A worker node is a physical machine that is capable of running containers e.g. a virtual machine as EC2 instance on AWS.
  - We can have more than one pods running on a worker node.

* ***Proxy:***
  - A proxy is setup on a worker node by Kubernetes.
  - Kubernetes proxies are used to connect to the outside world.

* When working with kubernetes, we typically need at least one worker node.
* Multiple pods can be created/removed to scale up/down the application.
* We can have different or equal containers running on multiple worker nodes to distribute the load evenly.
* All the worker nodes, pods and the containers running on them need to be controlled e.g. creation, replacement and removal of pods and containers.
* Master node is used to perform creation, replacement or removal of pods and containers using `Control Plane`.
* The control plane's components make global decisions about the cluster (for example, scheduling), as well as detecting and responding to cluster events (for example, starting up a new pod when a deployment's replicas field is unsatisfied).
* Control plane components can be run on any machine in the cluster. However, for simplicity, set up scripts typically start all control plane components on the same machine, and do not run user containers on this machine.
* To ensure high availability the control plane is also setup across multiple machines.
* The control plane is a collection of different tools and services.
* All these things together (worker and master nodes) form a cluster as seen below:

<p align="center">
<img src="images/components-of-kubernetes.svg">
</p>

* The kubernetes sends all this information to the cloud provider API to create all the resources needed for the cluster desired state.


### 1.4 Kubernetes and Developer Responsibilities:
* Kubernetes will not manage our infrastructure.
* Developer is responsible for creating the cluster and the node instances (worker+master nodes).
* Developer is responsible for setting up API server, kubelet and other kubernetes components on nodes.
* Developer is also responsible for creating cloud provider specific resources such as Load Balancers, Storage, etc. 
* Kubernetes create our object (e.g. pods) and manage them, it will create them automatically distribute them.
* Kubernetes will monitor, re-create and scale up/down the pods.
* Kubernetes utilizes the provided cloud resources to apply our configurations/goals.

### 1.5 Kubernetes Worker Node:
* Worker node can be thought of as a virtual machine e.g. and EC2 instance.
* The worker node is managed by the master node.
* Inside of a worker node we can have one or more pods. 
* A pod can hosts one or more application containers and their resources (e.g. volumes, IP, run config).
* Pods are created and managed by kubernetes i.e. by master node.
* `kubelet` is the component that runs on the worker node and responsible for communication between worker node and master node, so that master node can manage the pods on the worker node.
* `kube-proxy` also runs on the worker node and is responsible for handling incoming and outgoing traffic and only allowed traffic is able to reach the pods.

### 1.6 Kubernetes Master Node:
* `API Server` is the most important component of the kubernetes running on the master node. It is counter point to the `kubelet` service running on the worker node. It is responsible for handling communication between the worker nodes and the master node.
* `Scheduler` is responsible for watching our pods and choosing worker nodes where new pods should be created on. 
* `Kube-Controller-Manager` watches and control worker nodes and ensures correct number of pods are up and running and work closely with `Scheduler` and `API Server`.
* `Cloud-Controller-Manager` is similar to `Kube-Controller-Manager` but for a specific cloud provider and knows how to interact with the cloud provider resources.
* Big Cloud providers like AWS, GCP, Azure, etc. already have services available (e.g. EKS, GKE, AKS, etc.) that can be used to create and manage the cluster and we don't need to create and manage the cluster ourselves.
* We just need to provide our kubernetes configuration and the respective cloud provider will do all the heavy lifting.


# 2. Kubernetes Hands on:

### 2.1 Kubernetes doesn't manage the infrastructure:
* Kubernetes does not manage the infrastructure e.g. setting up VMs, keeping them update and maintaining them.
* Or setting up master and worker nodes, these are the things we need to do either manually or by using a tool like `kubermatic` or by using a kubernetes managed service by a cloud provider such as Amazon EKS.
* Followin is the comparison what Kubernetes can do and what we need to do.

<p align="center">
<img src="images/kubernetes_not_manage_infra.png" width=600>
</p>

### 2.2. Kubernetes Objects:
* Kubernetes work with so called objects e.g. pods, services, deployments, services, volume etc.
* Kubernetes objects are the objects that are created by Kubernetes and managed by it.
* We can create a certain object by executing a certain command.
* The objects can be created in two different ways imperatively or declaratively.
* Pods are designed to be ephemeral, kubernetes will start stop and replace them as needed.
* Pods share a lot of concepts of containers.
* Kubernetes manages the pods for us i.e. the whole deployment of applications.

### 2.3. Deployment Object:
* We don't create a pod object our own instead we create deployment object, and give it instructions about number of pods and teh containers that it should create and manage for us.
* Deployment object can create and manage multiple pods. The Deployment object is under the hood is the controller object.
* We describe a desired state in a Deployment, and the Deployment Controller changes the actual state to the desired state at a controlled rate.
* It define which Pods and containers to run and the number of Pods to run and where to place these pods i.e. on which machines.
* Deployments can be paused, deleted and rolled back.
* Deployments can also be scaled dynamically and automatically i.e. autoscaling on the basis of certain metrics. 
* Deployment can be created by specifying following command:

```bash
kubectl create deployment first-app --image=irdanish11/kub-first-app-01
```
* Make sure the image is available on a container registry because locally created images will not work and the deployment will fail.
* We can check the status of deployment and pods by following commands:

```bash
kubectl get deployment
kubectl get pods
```


### 2.4. Kubernetes Services:
* When we create deployment object, at that time we can't reach the Pod or the container running inside the container.
* To reach the Pod or the Container running inside the Pod, we need a service.
* The Services are responsible to expose pods to other pods on the cluster or to the visitors outside the cluster i.e. to thw world.
* Pod does have an IP address, we can't use that to access the pod outside from the cluster and secondly it changes when a pod is replaced. 
* Services group pods with a shared IP address and that IP address wont change.
* We can use Services to move multiple pods into a service to make them reachable on that service using unchanging IP addresses.
* The default a service is internal only but we can override it to make that service accessible externally.
* Without Services Pods are hard to reach even within the cluster because of the changing IP addresses problem.
* Instead of using `kubectl service` we can use `kubectl expose` command to expose a service.

```bash
kubectl expose deployment first-app --type=LoadBalancer --port=8080
```

* The `--port` flag specifies the port of the application which is exposed as in our case we've exposed port `8080` in our Dockerfile.
* The `--type` flag specifies the type of service we want to create. There are many options available, the default option is `ClusterIP`, which is used to create a service that is accessible from within the cluster.
* The other option is `NodePort`, which is used to connect to the service from outside the cluster.
* Another option is `LoadBalancer`, which is used to create a service that is accessible from outside the cluster along with the benefits of a load balancer. 
* The `LoadBalancer` option only works if our infrastructure supports it, AWS supports the `LoadBalancer` option and `minikube` also supports it.
* We can check whether the service is created successfully by following command:

```bash
kubectl get services
```
* In the `minikube` environment, the `EXTERNAL-IP` will always have `<pending>` status, the private IP will be assigned only when we are running Kubernetes on a Cloud.
* `minikube` have a command that will give us access to the service by mapping a port to an IP which we can reach from our local machine.
* The command is as follows:
  
```bash
minikube service first-app
```
* This will give us an IP address to access our service.
* The approach that we have used here is `imperative`, because we have defined the flow of the execution of different tasks.


### 2.5. Kubernetes Scaling:
* Let's say we haven't set up autoscaling, so kubernetes will not be creating or removing pods automatically but we have to do this manually.
* So we can manually set scaling i.e. replicas of a deployment.
* We can take advantage of load balancing because our deployment is using `LoadBalancer` option, which automatically balance the traffic between any number of pods that are available.
* We scale our deployment using following command:

```bash
kubectl scale deployment first-app --replicas=3
```

* The `--replicas` flag specifies the number of replicas of the pods that we want to create.
* We can scale down to any number of pods by using the same command but providing less number of replicas e.g. now we'll scale down to 1 pod.

```bash
kubectl scale deployment first-app --replicas=1
```

### 2.6. Updating the Deployment:
* Now let's say have updated our application and as a result we want to update the deployment as well.
* To do that first we need to re-build our image and push to the DockerHub or any container registry.
* Now its time to update our deployment, and to do that we can use the following command:

```bash
kubectl set image deployment/first-app kub-first-app-01=irdanish11/kub-first-app-01
```

* If we just run the above command we'll not see and update because kucbectl will not update the deployment if the image is the same.
* The image is same because we haven't updated the tag of the image.
* So in order to do that we need to build our images with tags, and the tag could be an incrementing number of maybe current datetime.

```bash
docker build -t irdanish11/kub-first-app-01:2 .
```
* Or maybe we can use date time:

```bash
docker build -t irdanish11/kub-first-app-01:$(date +%Y%m%d%H%M) .
```

* Now we will use the tag of the image and all will be good:

```bash
kubectl set image deployment/first-app kub-first-app-01=irdanish11/kub-first-app-01:2
```

* We can view the current updating status by running the following command:

```bash
kubectl rollout status deployment/first-app
```

### 2.7. Deployments Rollback and History:
* Now let's update our Deployment with an image tag that doesn't exist:

```bash
kubectl set image deployment/first-app kub-first-app-01=irdanish11/kub-first-app-01:2
```

* Now let's check the status of the deployment update:

```bash
kubectl rollout status deployment/first-app
```

* Now as this image does not exist the output of the above command will look like this:

```bash
Waiting for deployment "first-app" rollout to finish: 1 old replicas are pending termination...
```

* That means that the old pod has not terminated yet, why its not terminated we can check that in our `dashboard` under `pods` option or by using `kubectl get pods` command.
* The reason for old replica to be not terminated yet is that because the new replica is not starting up successfully and it is facing issues pulling the image.
* Kubernetes uses a rolling update strategy to update the pods i.e. first it create the new replica, once the new replica is created successfully, only then it removes the old replica.
* So in our case update never finishes, and in that case we need to rollback this update.
* To rollback we can use the following command:

```bash
kubectl rollout undo deployment/first-app
```

* Now we can check the status of the deployment rollback:

```bash
kubectl rollout status deployment/first-app
```

* Now the update/rollback is successfully.
* We can check the history of the deployment by using the following command:

```bash
kubectl rollout history deployment/first-app
```

* We can also have details about the deployment by using the following command:

```bash
kubectl rollout history deployment/first-app --revision=1
```

* The `--revision` flag specifies the revision of the deployment we want to see the history of.
* We can see that revision 1 is our orignal deployment.
* Now let's say we want to go back to the original deployment to do that we just need to use the `--to-revision` flag and provide the revision identifier to the flag along with our `rollout undo` command.

```bash
kubectl rollout undo deployment/first-app --to-revision=1
```

* Until now whatever we have done is by `imperative` approach next we'll do everything by using `declarative` approach.
* Now let's cleanup what we've created until now by using following commands:
  
```bash
kubectl delete service first-app
kubectl delete deployment first-app
```