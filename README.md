# CloudStruct: Multi-Tier Web App on AWS

## Overview
This repository provides an automated setup for a scalable, multi-tier web application on AWS. The project uses Terraform for Infrastructure as Code (IaC) to provision AWS resources such as EC2, RDS, S3, and IAM roles. It features Docker for containerization and Bash scripts for automation, ensuring efficient and maintainable deployment pipelines.

## Features
- **AWS Infrastructure**: Automates the setup of EC2 instances, RDS PostgreSQL, S3 buckets, and IAM roles.
- **Multi-Tier Architecture**: Separates the application, database, and storage tiers for scalability and reliability.
- **Infrastructure as Code**: Uses Terraform to provision and manage AWS resources.
- **Automation**: Includes Bash scripts for application deployment and database backups.
- **Containerized Environment**: Docker ensures consistent development and testing environments.

## Technologies Used
- **Cloud Platform**: AWS (EC2, RDS, S3, IAM)
- **Database**: PostgreSQL on RDS
- **IaC**: Terraform
- **Containerization**: Docker, Docker Compose
- **Automation**: Bash Scripts

## Prerequisites
- Install [Terraform](https://www.terraform.io/)
- Install [Docker](https://www.docker.com/)
- Install [Git](https://git-scm.com/)
- AWS account with programmatic access
- Basic knowledge of Terraform and Bash scripting

## Setup Instructions

### 1. Clone the Repository
Clone this repository to your local machine and navigate into the directory:
```bash
git clone https://github.com/Rt0727/CloudStruct-Multi-Tier-Web-App-on-AWS.git
cd CloudStruct-Multi-Tier-Web-App-on-AWS
```

### 2. Configure Terraform Variables
Create a `.tfvars` file in the `terraform/` directory with the following contents:
```hcl
aws_region        = "us-east-1"
instance_type     = "t2.micro"
db_instance_class = "db.t2.micro"
db_name           = "webapp_db"
db_username       = "admin"
db_password       = "password"
bucket_name       = "webapp-storage-bucket"
```

### 3. Initialize and Deploy Infrastructure
Use Terraform to initialize and deploy the necessary AWS resources:
```bash
cd terraform
terraform init
terraform apply -var-file="variables.tfvars"
```
This will provision:
- EC2 instances for the application.
- An RDS PostgreSQL database with multi-AZ deployments.
- S3 bucket for storage.
- IAM roles for secure resource access.

### 4. Build and Start Docker Containers (Local Testing)
For local testing, navigate back to the root directory and use Docker Compose to start the application:
```bash
docker-compose up --build
```
This will:
- Build the Docker image for the web application.
- Start the application in a local environment.

### 5. Deploy Application to AWS
Use the provided script to deploy the application to AWS EC2 instances:
```bash
./scripts/deploy.sh
```

### 6. Use Backup Script
Automate database backups with the provided script:
```bash
./scripts/backup.sh
```
This script ensures the safety of your PostgreSQL data by storing backups securely.

## Project Structure
```plaintext
multi-tier-webapp-infrastructure-setup/
│
├── terraform/
│   ├── main.tf                    # Defines EC2, RDS, S3, IAM resources
│   ├── variables.tf               # Contains variable definitions
│   └── outputs.tf                 # Outputs application endpoint and RDS details
│
├── docker/
│   ├── Dockerfile                 # Dockerfile for multi-tier application
│   └── docker-compose.yml         # Docker Compose for local testing
│
├── scripts/
│   ├── backup.sh                  # Backup script for PostgreSQL database
│   └── deploy.sh                  # Deployment script for AWS EC2 instances
│
├── README.md                      # Documentation
└── .gitignore                     # Git ignore file
```

## Troubleshooting

### Common Issues
1. **Terraform Errors**: Ensure Terraform is installed, and the `variables.tfvars` file is correctly configured.
2. **AWS Resource Errors**: Verify that your AWS account has sufficient permissions to create resources.
3. **Docker Issues**: Ensure Docker is running and containers are built successfully.

### Logs
Access logs for debugging:
- Terraform logs: Check `terraform.tfstate` for resource state.
- Application logs (local): Run `docker-compose logs app`.

## Future Enhancements
- Add a CI/CD pipeline for automated deployments.
- Implement monitoring with AWS CloudWatch for enhanced observability.
- Integrate advanced analytics for application performance insights.

---

For any questions or issues, feel free to reach out at `your.email@example.com`.

--- 