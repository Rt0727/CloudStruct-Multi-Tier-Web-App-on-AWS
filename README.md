# CloudStruct: Multi-Tier Web App on AWS

## Overview
This repository provides an automated setup for a scalable, multi-tier web application on AWS. The project uses Terraform for Infrastructure as Code (IaC) to provision AWS resources such as EC2, RDS, S3, and IAM roles. It features Docker for containerization, Bash scripts for automation, and Python for managing AWS resources, ensuring efficient and maintainable deployment pipelines.

## Features
- **AWS Infrastructure**: Automates the setup of EC2 instances, RDS PostgreSQL, S3 buckets, and IAM roles.
- **Multi-Tier Architecture**: Separates the application, database, and storage tiers for scalability and reliability.
- **Infrastructure as Code**: Uses Terraform to provision and manage AWS resources.
- **Automation**: Includes Bash scripts for application deployment and database backups, along with Python scripts for managing AWS resources.
- **Containerized Environment**: Docker ensures consistent development and testing environments.
- **Python Integration**: Python scripts automate EC2, RDS, S3, and IAM management tasks.

## Technologies Used

| Technology                   |  Purpose                             |
|------------------------------|--------------------------------------|
| **PostgreSQL**               | Database for library data            |
| **Docker**                   | Containerization                     |
| **Terraform**                | Infrastructure provisioning          |
| **Bash Scripts**             | Automation of routine tasks          |
| **AWS (EC2, RDS, S3, IAM)**  | Core application logic for the CLI   |

## Prerequisites
- Install [Terraform](https://www.terraform.io/)
- Install [Docker](https://www.docker.com/)
- Install [Git](https://git-scm.com/)
- Install [Python](https://www.python.org/) and [boto3](https://pypi.org/project/boto3/)
- AWS account with programmatic access
- Basic knowledge of Terraform, Docker, and Python scripting

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
Use the provided Python script to deploy the application to AWS EC2 instances:
```bash
python python/app_deploy.py
```

### 6. Manage AWS Resources (EC2, RDS, S3, IAM)
Python scripts for managing AWS resources:
- **EC2 Management**: `python/ec2_manager.py`
- **RDS Management**: `python/rds_manager.py`
- **S3 Management**: `python/s3_manager.py`
- **IAM Management**: `python/iam_manager.py`

You can use these Python scripts for additional AWS resource management:
```bash
python python/ec2_manager.py
python python/rds_manager.py
python python/s3_manager.py
python python/iam_manager.py
```

### 7. Use Backup Script
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
├── python/
│   ├── app_deploy.py              # Python script to deploy the web app to AWS
│   ├── ec2_manager.py             # Python script for managing EC2 instances
│   ├── rds_manager.py             # Python script to manage RDS instances
│   ├── s3_manager.py              # Python script to manage S3 buckets
│   ├── iam_manager.py             # Python script to manage IAM roles/policies
│   └── tests/
│       ├── test_ec2_manager.py    # Unit tests for EC2 management
│       ├── test_rds_manager.py    # Unit tests for RDS management
│       ├── test_s3_manager.py     # Unit tests for S3 management
│       └── test_iam_manager.py    # Unit tests for IAM management
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
4. **Python Errors**: Ensure you have installed the necessary dependencies (`boto3`) and configured AWS credentials.

### Logs
Access logs for debugging:
- Terraform logs: Check `terraform.tfstate` for resource state.
- Application logs (local): Run `docker-compose logs app`.
- Python script logs: Check the Python console output for any errors related to resource management.

## Future Enhancements
- Add a CI/CD pipeline for automated deployments.
- Implement monitoring with AWS CloudWatch for enhanced observability.
- Integrate advanced analytics for application performance insights.

```

For any questions or issues, feel free to reach out at `rt07mahifan@gmail.com`.

--- 
