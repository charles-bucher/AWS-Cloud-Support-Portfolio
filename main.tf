terraform {
  required_version = ">= 1.5.0"
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

provider "aws" {
  region = var.aws_region
}

# Data: Availability Zones
data "aws_availability_zones" "available" {}

# VPC
resource "aws_vpc" "lab_vpc" {
  cidr_block = var.vpc_cidr
  tags = { Name = "lab-vpc" }
}

# Public Subnet
resource "aws_subnet" "public_subnet" {
  vpc_id            = aws_vpc.lab_vpc.id
  cidr_block        = var.public_subnet_cidr
  map_public_ip_on_launch = true
  availability_zone = data.aws_availability_zones.available.names[0]
  tags = { Name = "lab-public-subnet" }
}

# Security Group
resource "aws_security_group" "lab_sg" {
  name        = "lab-security-group"
  description = "Allow SSH, HTTP, ICMP"
  vpc_id      = aws_vpc.lab_vpc.id

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

  ingress {
    from_p_
