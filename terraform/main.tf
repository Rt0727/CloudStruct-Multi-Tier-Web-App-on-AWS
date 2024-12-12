provider "aws" {
  region = "us-west-2"
}

resource "aws_instance" "web_app_server" {
  ami           = "ami-0abcdef1234567890"  # Replace with the latest AMI ID
  instance_type = "t2.medium"
  key_name      = var.key_name
  tags = {
    Name = "web-app-server"
  }
}

resource "aws_security_group" "web_app_sg" {
  name_prefix = "web-app-sg"
  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
  ingress {
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

resource "aws_rds_instance" "app_db" {
  allocated_storage = 20
  storage_type      = "gp2"
  engine            = "mysql"
  engine_version    = "8.0"
  instance_class    = "db.t2.micro"
  db_name           = "app_database"
  username          = var.db_username
  password          = var.db_password
  parameter_group_name = "default.mysql8.0"
}

resource "aws_s3_bucket" "app_bucket" {
  bucket = "multi-tier-web-app-bucket"
}

resource "aws_iam_role" "app_role" {
  name = "app-role"
  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Action    = "sts:AssumeRole"
        Principal = {
          Service = "ec2.amazonaws.com"
        }
        Effect    = "Allow"
        Sid       = ""
      },
    ]
  })
}