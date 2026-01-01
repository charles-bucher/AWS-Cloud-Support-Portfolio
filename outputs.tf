output "vpc_id" {
  description = "VPC ID"
  value       = aws_vpc.lab_vpc.id
}

output "public_subnet_id" {
  description = "Public subnet ID"
  value       = aws_subnet.public_subnet.id
}

output "security_group_id" {
  description = "Security Group ID"
  value       = aws_security_group.lab_sg.id
}

output "instance_public_ip" {
  description = "EC2 public IP"
  value       = aws_instance.lab_instance.public_ip
}

output "s3_bucket_name" {
  description = "Lab S3 bucket"
  value       = aws_s3_bucket.lab_bucket.bucket
}
