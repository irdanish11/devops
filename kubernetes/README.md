
# 1. Introduction to Kubernetes

### 1.1 What is Kubernetes?

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
  - Kubernetes requires a little more expertise. If you are on EKS, you will have the benefit of setting up through the AWS Management Console, but you will still need to configure and deploy pods via Kops.
  - Kubernetes has much higher limits in general — even supporting up to 750 pods per instance on EKS. These limits may look very important at first glance, but become critical when deploying large apps that require thousands of pods and nodes.
  - Kubernetes, offers flexibility and customizability and we can access cluster nodes and pods directly.