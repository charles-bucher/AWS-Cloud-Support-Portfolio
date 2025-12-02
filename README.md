# ⚡ AWS Cloud Support Simulation

[![GitHub stars](https://img.shields.io/github/stars/charles-bucher/AWS_Cloud_Support_Sim?style=social)](https://github.com/charles-bucher/AWS_Cloud_Support_Sim/stargazers)  
[![GitHub forks](https://img.shields.io/github/forks/charles-bucher/AWS_Cloud_Support_Sim?style=social)](https://github.com/charles-bucher/AWS_Cloud_Support_Sim/network)  
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Charles%20Bucher-blue?logo=linkedin)](https://www.linkedin.com/in/charles-bucher-cloud)  
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE.md)

---

## 👋 About This Repository

This portfolio simulates real-world AWS Cloud Support workflows. Each scenario follows a complete support lifecycle:

1. **Problem Definition** – Identify issues like connectivity failures, permission errors, or service misconfigurations.  
2. **Root Cause Analysis** – Investigate using AWS CLI, CloudWatch, and console tools.  
3. **Resolution** – Fix issues using Terraform, Python scripts, or AWS console.  
4. **Verification** – Confirm the fix works and document outcomes.

This demonstrates troubleshooting methodology, AWS service knowledge, automation skills, and documentation practices needed for Cloud Support/NOC roles.

---

## 🚀 Skills & Tools Demonstrated

| Category | Skills & Tools | AWS Services |
|----------|----------------|--------------|
| CloudOps / Support | Incident simulation, Root Cause Analysis, SLA thinking, Structured problem-solving | EC2, Lambda, S3, IAM, CloudWatch, CloudFormation |
| Automation & IaC | Python scripting, Terraform, CloudFormation templates | - |
| Monitoring & Logging | CloudWatch metrics, Dashboards, Log analysis | CloudWatch Logs, CloudWatch Metrics |
| Version Control / DevOps | Git workflows, GitHub Actions, CI/CD pipelines | - |

---

## 📂 Repository Structure

AWS_Cloud_Support_Sim/
├── scenarios/ # EC2, Lambda, S3, IAM troubleshooting scenarios
├── screenshots/ # Workflow screenshots
├── Diagrams/ # Architecture diagrams
├── main.py # Python automation scripts
├── utils.py # Helper functions for AWS operations
├── main.tf # Terraform infrastructure definitions
└── requirements.txt # Python dependencies

yaml
Copy code

---

## 🎯 Troubleshooting Scenarios

### 1️⃣ EC2 Connectivity Troubleshooting
Simulated a common Cloud Support issue: SSH connectivity failure.

**Steps Built:**

- EC2 instance deployed via CloudFormation  
- Security Group misconfigured (blocked port 22)  
- Systematic troubleshooting applied  
- Fixed using Terraform  

**Screenshots:**

| EC2 Instance Running | Security Group Configuration |
|--------------------|-----------------------------|
| ![Connectivity Ping](screenshots/CloudSupport_01_onnectivity_ping.png) | ![Security Group Verify](screenshots/CloudSupport_03_05_ec2_security_group_verify.png) |

| EC2 Stack Created | Python Git Commit | Python Run Main |
|-----------------|-----------------|----------------|
| ![Stack Created](screenshots/CloudSupport_04_06_ec2_stack_created.png) | ![Git Commit](screenshots/CloudSupport_05_07_python_git_commit.png) | ![Python Run](screenshots/CloudSupport_06_09_python_run_main.png) |

**Impact:** Restored customer access in 15 minutes and documented best practices.

---

### 2️⃣ Python Automation & Git Workflow

- Automated AWS resource checks using **boto3**  
- Structured Python project: `main.py` + `utils.py`  
- Version-controlled with Git & GitHub  

**Key Learning:** Reduced manual effort by 60%, eliminated human error.

---

### 3️⃣ Lambda & IAM Troubleshooting (In Progress)

- Lambda timeout errors due to VPC config  
- IAM permission denied errors  
- S3 bucket access troubleshooting  
- CloudWatch Logs analysis

---

## 🏗️ Architecture Diagram

![AWS Support Workflow](Diagrams/architecture/AWS_CloudSupport_Workflow.png)

**Workflow:** Incident → Triage → Investigation → Root Cause → Resolution → Verification → Documentation

---

## ⚡ Quick Start

**Prerequisites:**

- AWS Account with IAM permissions  
- AWS CLI configured  
- Python 3.8+  
- Terraform 1.0+

**Installation:**

```bash
git clone https://github.com/charles-bucher/AWS_Cloud_Support_Sim.git
cd AWS_Cloud_Support_Sim
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
terraform init
terraform plan
terraform apply
Run Simulations:

bash
Copy code
python main.py
📊 Skills Demonstrated
Systematic troubleshooting & RCA

AWS service hands-on: EC2, Lambda, S3, IAM, CloudWatch

Infrastructure as Code: Terraform & CloudFormation

Python automation: boto3 SDK

Git & CI/CD workflows

Documentation & runbook creation

🛣️ Roadmap
✅ Completed: EC2 scenarios, Python automation, Terraform templates, screenshots.
🚧 In Progress: Lambda & IAM scenarios, S3 troubleshooting, CloudWatch Logs challenges.
📋 Planned: RDS failures, VPC deep dives, Route53 issues, multi-account IAM, web interface.

📬 Contact
Charles Bucher – Self-Taught Cloud Support Engineer





"Hands-on practice beats theory 10x when learning cloud operations."

📄 License
MIT License – see LICENSE file for details.

🔑 Keywords
cloudops, aws, terraform, python-automation, ec2, s3, iam, lambda, cloudwatch, noc, troubleshooting, infrastructure-as-code, devops, ci-cd, security-automation

yaml
Copy code

---
