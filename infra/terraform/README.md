# ECS deployment with Terraform

This Terraform template provisions:
- a VPC and public subnets
- an Application Load Balancer
- an ECS Fargate cluster and service
- a task definition for the FastAPI weather app

## Prerequisites
- AWS credentials configured
- an ECR image URI for your container

## Usage
1. Copy terraform.tfvars.example to terraform.tfvars
2. Set your container image value
3. Run:

```bash
terraform init
terraform plan -var-file=terraform.tfvars
terraform apply -var-file=terraform.tfvars
```

The ALB DNS name will be printed as an output.
