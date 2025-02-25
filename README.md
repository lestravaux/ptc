# Python API Server with Docker, IaC, Kubernetes & CI/CD

## Overview
The solution includes:

- **Python API server**: app/ -> Python API server with two endpoints: GET /users (retrieve all users) and POST /user (create a new user) (initiated from AI tools)
- **Dockerisation**: Dockerfile -> Dockerfile to containerize the application. 
- **Infrastructure as Code**: terraform-eks/ -> Terraform scripts to provision an AWS EKS cluster. (initiated from https://github.com/hashicorp-education/learn-terraform-provision-eks-cluster)
- **Kubernetes Deployment**: helm-ptc-chart/ -> A Helm chart to deploy the Python application. (initiated with helm create cmd)
- **CI/CD Pipeline**: .github/workflows/ci-cd.yml -> A GitHub Actions workflow for building, testing, and deploying the application.

ptc/
├── app/
│   ├── main.py              # Python API server using FastAPI
│   ├── database.py          # Database connection and ORM setup
│   ├── models.py            # SQLAlchemy models for user data
│   ├── requirements.txt     # Python dependencies
│   └── tests/
│       └── test_api.py      # Unit tests for the API endpoints
├── Dockerfile               # Containerization of the API server
├── .dockerignore           # Files to ignore in Docker builds
├── terraform-eks/
│   ├── main.tf              # Terraform configuration for EKS
│   ├── variables.tf         # Variables for Terraform configuration
│   ├── outputs.tf           # Terraform outputs (e.g., cluster name)
│   └── terraform.tfstate    # Terraform state file (local or remote)
├── helm/
│   └── ptc-chart/           # Helm chart for deploying the API
│       ├── Chart.yaml
│       ├── values.yaml      # Default values (e.g., image.repository, replicaCount)
│       └── templates/
│           └── deployment.yaml  # Kubernetes Deployment manifest template
├── .github/
│   └── workflows/
│       └── cicd.yml         # GitHub Actions workflow definition for CI/CD
└── README.md                # This file

## Prerequisites
- Ubuntu Linux
- Python 3.8+
- Docker
- Terraform (v1.0+ recommended)
- Helm (v3+)
- kubectl
- AWS CLI configured with AWS credentials for EKS
- Helm & kubectl
- GitHub repository with Github Actions for CI/CD

## Getting Started

## Terraform: Infrastructure provisioning of EKS

1. Navigate to the `terraform-eks/` directory.
2. Provided AWS CLI and credentials are configured, Run ```terraform plan``` and ```terraform apply``` to provision the AWS EKS cluster
3. Store the ```CLUSTER_NAME``` as a secret/variable in Settings -> Security -> Secrets and Variables

## CI/CD Pipeline

The CI/CD pipeline is defined in .github/workflows/cicd.yml. The pipeline performs the following steps:

Checkout Code:
Pulls the latest repository code.

Set Environment Variables:
Computes the IMAGE_TAG based on the Git commit hash and writes it to $GITHUB_ENV.

Security Scanning:
Runs security scans on Python code, dependencies, and container images using tools such as Bandit, Trivy, and Checkov.

Terraform Deployment:
Uses Terraform to provision an AWS EKS cluster along with necessary IAM roles, VPC, and node groups.

Helm Deployment:
Deploys the Python API to the EKS cluster using a Helm chart. The image repository and tag values are set dynamically from GitHub Secrets and environment variables.



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
     