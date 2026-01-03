# -----------------------------
# Outputs
# -----------------------------

output "vpc_id" {
  value = aws_vpc.lab_vpc.id
}

output "instance_id" {
  value = aws_instance.lab_instance.id
}

output "instance_public_ip" {
  value = aws_instance.lab_instance.public_ip
}

output "s3_bucket_name" {
  value = aws_s3_bucket.lab_bucket.id
}

output "ssh_command" {
  value = "ssh -i ~/.ssh/${var.key_pair_name}.pem ec2-user@${aws_instance.lab_instance.public_ip}"
}

output "security_status" {
  value = <<-EOT
  ===== SECURITY STATUS =====
  ✅ SSH restricted to: ${var.my_ip_address}
  ✅ S3 encryption: Enabled
  ✅ S3 public access: Blocked
  ✅ IMDSv2: Enforced
  ✅ EBS encryption: Enabled
  ===========================
  EOT
}
