# DevOps Demo App
## Overview
- This is the repo for running python-flask app under mod_wsgi on apache in a docker container. It has two sample endpoints returning JSON response viz. 'Hello World' and application health status respectively.  
- Its configured for standard code and docker checks with Jenkins. 
- Finally docker container can be deployed on Kubernetes cluster as 'Deployment-ReplicaSet' with Load Balancer service to provide high availability. 
## Solution Decisions
**Web Framework: Flask** \
Flask is a lightweight and flexible micro web framework for Python. It's well-suited for small to medium-sized applications and allows for quick development. \
**Code Linting: Flake8** \
Flake8 is used for linting to ensure code consistency and identify potential issues. It checks for PEP 8 compliance and can be customized with additional plugins for more checks. \
**Testing Framework: unittest** \
Python's built-in unittest module is used for writing and running tests. It provides a test discovery mechanism and assertions for verifying expected outcomes. \
**Container Linting: hadolint** \
hadolint is used to lint the Dockerfile to ensure best practices for creating Docker images. It checks for common mistakes and enforces best practices in Dockerfile creation. \
**Containerization: Docker** \
Docker is used for containerization to ensure that the application runs consistently across different environments. It simplifies deployment and dependency management. \
**Containerization: Kubernetes** \
Kubernetes LoadBalancer service along with Deployment-Replicaset provides various solution advantages such as high availablity, scalability, business continuite during system maintenance, etc. 

## Automation with Jenkins
Jenkins pipeline has below 4 stages and configuration available in Jenkinsfile. 
- Checkout: This stage checks out the source code from the specified Git repository 
- Lint: Lint: In this stage, the flake8 linter is using to validate Python code files.
- Test: This stage runs Python test cases using unittest to verify each endpoint. 
- Docker Lint: This stage uses hadolint to lint the Dockerfile. Please note this file needs to be updated in future to remedy 'DL3008'.    

## Steps to deploy on Kubernetes Cluster
- Build docker image 
```
docker build -t devops-demo .
```
- Deploy on local Kubernetes cluster 
```
kubectl apply -f deployment.yaml
```
- Access endpoints using localhost (requires additional configuration for Production) 
```
http://localhost:80
```
```
http://localhost:80/health
```

## Stack Information
Python Version: Python 3.8 \
Editor: Any Text Editor or IDE (Used Visual Code) \
Web Framework: Flask (a micro web framework for Python) \
Automation: Jenkins
Linting Tool: Flake8 \
Testing Framework: unittest \
Containerization Tool: Docker \
Container Linting Tool: hadolint 