
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