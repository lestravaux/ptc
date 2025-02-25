# Python API Server with Docker, IaC, Kubernetes & CI/CD

## Overview
This repository contains a Python API server with two endpoints:
- **GET /users**: Retrieve all users.
- **POST /user**: Create a new user.

The solution includes:
- **Dockerisation**: A Dockerfile to containerize the application.
- **Infrastructure as Code**: Terraform scripts to provision an AWS EKS cluster.
- **Kubernetes Deployment**: A Helm chart to deploy the API server.
- **CI/CD Pipeline**: A GitHub Actions workflow for building, testing, and deploying the application.

## Prerequisites
- Ubuntu Linux
- Docker
- Terraform (if provisioning infrastructure)
- AWS CLI and proper AWS credentials for EKS
- Helm & kubectl
- GitHub account for CI/CD

## Getting Started

### Local Development
1. Navigate to the `api/` directory.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt


curl -X POST http://127.0.0.1:8000/user \
     -H "Content-Type: application/json" \
     -d '{"name": "Denis Fongang", "email": "fongang@outlook.fr"}'

curl -X POST http://127.0.0.1:8000/user -H "Content-Type: application/json" -d '{"name": "rien", "email": "rien@outlook.fr"}'

curl -X POST a63a5298a90ad43f0a08a08b9c8697e3-1128454918.us-east-2.elb.amazonaws.com:8000/user -H "Content-Type: application/json" -d '{"name": "Denis", "email": "fongang@outlook.fr"}'

     aws eks update-kubeconfig --region us-east-2 --name 
     kubectl create namespace argocd
     kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml
     k get po -n argocd
     kubectl patch svc argocd-server -n argocd -p '{"spec": {"type": "LoadBalancer"}}'
     k get svc -n argocd
     kubectl -n argocd get secret argocd-initial-admin-secret -o jsonpath="{.data.password}" | base64 -d
     