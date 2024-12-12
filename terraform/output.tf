output "public_ip" {
  value = aws_instance.web_app_server.public_ip
}

output "rds_endpoint" {
  value = aws_rds_instance.app_db.endpoint
}

output "s3_bucket" {
  value = aws_s3_bucket.app_bucket.bucket
}