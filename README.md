# AWS Cloud Support Portfolio

This repository showcases hands-on troubleshooting scenarios for AWS services, demonstrating skills in EC2, Lambda, S3, IAM, and more. It is designed for entry-level cloud support positions.

---

## Table of Contents

1. [EC2 Troubleshooting](#ec2-troubleshooting)
2. [Lambda Error Handling](#lambda-error-handling)
3. [S3 IAM Access](#s3-iam-access)
4. [Screenshots](#screenshots)

---

## EC2 Troubleshooting

**Scenario:** Launch an EC2 instance via CloudFormation, verify connectivity, and troubleshoot security group issues.  

**Files:**

- `scenarios/ec2-troubleshoot/cloudformation.yaml` – CloudFormation template
- `scenarios/ec2-troubleshoot/ec2-troubleshoot.txt` – Step-by-step troubleshooting notes
- `scenarios/ec2-troubleshoot/instructions.md` – Instructions for setup

**Key Steps:**

1. Deploy the CloudFormation stack
2. Verify EC2 instance creation
3. Configure and check Security Groups
4. Test connectivity using ping and SSH

**Screenshots:**

![Stack Created](docs/screenshots/01_stack_created.png)
![Security Group Config](docs/screenshots/02_security_group.png)
![EC2 Instance](docs/screenshots/04_ec2.png)
![Security Group Details](docs/screenshots/05_security_group.png)
![Ping Connectivity](docs/screenshots/06_connectivity_ping_confirm.png)
![Ping Test](docs/screenshots/06_ping_test.png)

---

## Lambda Error Handling

**Scenario:** Diagnose and resolve a Lambda function error.

**Files:**

- `scenarios/lambda-error/instructions.md`

---

## S3 IAM Access

**Scenario:** Troubleshoot access issues for S3 buckets using IAM policies.

**Files:**

- `scenarios/s3-iam-access/instructions.md`

---

## Screenshots Overview

All screenshots are stored in `docs/screenshots/`. They demonstrate:

- CloudFormation stack creation
- EC2 instance deployment and connectivity
- Security Group verification
- Ping and network troubleshooting tests

---

## Contact

Charles Bucher  
[GitHub](https://github.com/charles-bucher)  
[LinkedIn](https://www.linkedin.com/in/charles-bucher-cloud)  

---

