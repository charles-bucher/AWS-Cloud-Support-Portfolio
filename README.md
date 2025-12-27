# AWS CloudOps Suite 🛠️

![Python](https://img.shields.io/badge/Python-3.9+-3776AB?logo=python&logoColor=white)
![Terraform](https://img.shields.io/badge/Terraform-1.0+-7B42BC?logo=terraform&logoColor=white)
![AWS](https://img.shields.io/badge/AWS-Cloud-FF9900?logo=amazon-aws&logoColor=white)
[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE.md)
![CloudOps](https://img.shields.io/badge/CloudOps-Automation-blue.svg)

> **Production-ready CloudOps automation toolkit for AWS infrastructure management, monitoring, and incident response**

Complete cloud operations suite featuring automated monitoring, security configuration, infrastructure as code, serverless functions, and CI/CD pipelines. Built to demonstrate enterprise-level CloudOps practices for entry-level cloud engineer roles.

---

## 🎯 What This Demonstrates

**Core CloudOps Skills:**
- ✅ Automated infrastructure deployment and management
- ✅ Real-time monitoring and alerting with CloudWatch
- ✅ Serverless automation with Lambda
- ✅ Security best practices (IAM, GuardDuty)
- ✅ CI/CD pipeline implementation
- ✅ Infrastructure validation and health checks

**Perfect for:** Cloud Engineer, DevOps, CloudOps, AWS Support, SRE positions

---

## ✅ Proof It Actually Works

### Automated Validation
![Validation Output](screenshots/02_validator_output.png)
*Custom validation tool ensuring infrastructure health and compliance*

### CI/CD Pipeline
![GitHub Actions](screenshots/27_ci_github_actions.png)
*Automated testing and deployment with GitHub Actions*

---

## 🚀 Quick Start

### Prerequisites

- **AWS Account** with admin access
- **AWS CLI** configured
- **Terraform** 1.0+ installed
- **Python** 3.9+ installed

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/charles-bucher/AWS_Cloudops_Suite.git
cd AWS_Cloudops_Suite

# 2. Set up Python environment
python -m venv venv
source venv/bin/activate          # Linux/Mac
.\venv\Scripts\activate           # Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run validation
python scripts/validate_system.py
```

### Deploy Infrastructure

```bash
# Initialize Terraform
cd tf
terraform init
terraform plan
terraform apply
```

![Terraform Apply](screenshots/23_tf_apply.png)
*Terraform deploying AWS infrastructure including Lambda, CloudWatch, IAM, and monitoring stack*

---

## 🛠️ Key Features

### 1. Infrastructure Automation

**Terraform-managed AWS resources:**
- Lambda functions for automated tasks
- CloudWatch monitoring and alarms
- DynamoDB for state management
- IAM roles and security policies
- VPC networking components

### 2. Monitoring & Observability

![CloudWatch Setup](screenshots/08_monitor_cloudwatch_confirm.png)
*CloudWatch monitoring configured for real-time infrastructure visibility*

![DynamoDB Monitoring](screenshots/09_monitor_dynamodb_confirm.png)
*DynamoDB metrics tracking for database performance*

![CPU Metrics](screenshots/14_metrics_cpu_1.png)
*Real-time CPU and performance metrics dashboard*

**Capabilities:**
- Automated health checks and validation
- CloudWatch Logs aggregation
- Custom metrics and dashboards
- DynamoDB performance monitoring
- Alert configuration and SNS notifications

### 3. Serverless Automation

![Lambda Functions](screenshots/13_lambda_functions.png)
*Deployed Lambda functions for automated CloudOps tasks*

**Lambda Functions:**
- Infrastructure health checks
- Automated incident response
- Cost optimization automation
- Security compliance validation
- Log processing and analysis

### 4. Security & Compliance

![IAM Configuration](screenshots/10_iam_roles.png)
*IAM roles and policies following AWS security best practices*

**Security Features:**
- Least privilege IAM policies
- GuardDuty threat detection
- Automated security audits
- Secrets management
- CloudTrail audit logging

### 5. CI/CD Pipeline

**GitHub Actions Workflows:**
- Automated testing on every commit
- Terraform validation and planning
- Python linting and code quality checks
- Security scanning
- Automated deployments to AWS

---

## 📂 Project Structure

```
AWS_Cloudops_Suite/
├── .github/
│   └── workflows/          # CI/CD automation
├── diagrams/               # Architecture diagrams
├── docs/                   # Documentation & runbooks
├── lambdas/                # Lambda function code
├── my_function/            # Custom Lambda functions
├── screenshots/            # Visual documentation
├── scripts/                # Automation scripts
│   ├── validate_system.py
│   └── health_check.py
├── src/                    # Core application code
├── tests/                  # Unit and integration tests
├── tf/                     # Terraform infrastructure
│   ├── main.tf
│   ├── lambda.tf
│   ├── monitoring.tf
│   └── security.tf
├── index.py                # Main Lambda handler
├── requirements.txt        # Python dependencies
└── README.md              # This file
```

---

## 🏗️ Architecture

### CloudOps Automation Flow

```
Developer → GitHub → CI/CD Pipeline → AWS Infrastructure
                ↓
         Automated Tests
                ↓
         Terraform Apply
                ↓
    ┌────────────────────────────┐
    │   AWS Cloud Environment    │
    ├────────────────────────────┤
    │ • Lambda Functions         │
    │ • CloudWatch Monitoring    │
    │ • DynamoDB Tables          │
    │ • IAM Roles & Policies     │
    │ • GuardDuty Security       │
    └────────────────────────────┘
                ↓
         CloudWatch Logs
                ↓
         Alert → SNS → Notifications
```

---

## 🔧 Tech Stack

### Cloud Platform
**AWS Services:**
- Lambda (Serverless compute)
- CloudWatch (Monitoring & logs)
- DynamoDB (Database)
- IAM (Security & access)
- GuardDuty (Threat detection)
- SNS (Notifications)
- EventBridge (Event routing)

### Infrastructure as Code
**Terraform** - Complete infrastructure automation

### Languages & Frameworks
- **Python 3.9+** - Automation scripts and Lambda functions
- **HCL** - Terraform configuration
- **Bash** - Shell scripting

### DevOps Tools
- **GitHub Actions** - CI/CD pipelines
- **pytest** - Testing framework
- **Git** - Version control

---

## 💡 Skills Demonstrated

### ☁️ Cloud Operations
- Multi-service AWS infrastructure management
- Automated monitoring and alerting
- Performance optimization
- Cost management
- Incident response automation

### 🏗️ Infrastructure as Code
- Terraform state management
- Module design and reusability
- Resource dependency management
- Infrastructure versioning

### 🤖 Serverless Architecture
- Lambda function development
- Event-driven automation
- Serverless best practices
- Error handling and retries

### 📊 Monitoring & Observability
- CloudWatch metrics and dashboards
- Custom metrics creation
- Log aggregation and analysis
- Alert configuration
- Performance monitoring

### 🔒 Cloud Security
- IAM policy design
- Least privilege principles
- Threat detection with GuardDuty
- Audit trail implementation
- Secrets management

### 🚀 DevOps Practices
- CI/CD pipeline design
- Automated testing
- Infrastructure validation
- Documentation as code
- GitOps workflows

---

## 📋 Use Cases

### 1. Automated Health Checks
Continuously monitor AWS infrastructure health and alert on issues

### 2. Cost Optimization
Identify and remediate cost inefficiencies automatically

### 3. Security Compliance
Validate security configurations and respond to threats

### 4. Incident Response
Automated detection and response to infrastructure issues

### 5. Performance Monitoring
Track and optimize application performance metrics

---

## 🎓 Getting Started Guide

### For Employers/Reviewers

1. **Review Architecture** - Check diagrams and infrastructure design
2. **Examine Code Quality** - Review Python and Terraform code
3. **Check CI/CD** - See GitHub Actions workflows
4. **Test Locally** - Clone and run validation scripts
5. **Review Documentation** - Explore docs/ folder

### For Learning

1. Start with `docs/setup.md` for detailed setup
2. Run `python scripts/validate_system.py` to understand validation
3. Deploy infrastructure with Terraform
4. Review Lambda functions in `lambdas/`
5. Customize and extend for your use cases

---

## 🤝 Contributing

Contributions are welcome! This is an active portfolio project.

**How to contribute:**
- 🐛 Report bugs via Issues
- 💡 Suggest new features
- 📝 Improve documentation
- ✨ Submit pull requests

---

## 📜 License

This project is licensed under the MIT License - see [LICENSE.md](LICENSE.md) for details.

---

## 🔒 Security

Found a security issue? Please report it responsibly via the [Security Policy](SECURITY.md).

---

## 📞 Connect With Me

**Charles Bucher** - Cloud Engineer | CloudOps Specialist

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Charles__Bucher-0A66C2?logo=linkedin&logoColor=white)](https://linkedin.com/in/charles-bucher-cloud)
[![GitHub](https://img.shields.io/badge/GitHub-charles--bucher-181717?logo=github&logoColor=white)](https://github.com/charles-bucher)
[![Portfolio](https://img.shields.io/badge/Portfolio-View-success?logo=github&logoColor=white)](https://charles-bucher.github.io)

---

## 🌟 Related Projects

- [AWS Cloud Support Simulator](https://github.com/charles-bucher/AWS_Cloud_Support_Sim) - 7 hands-on troubleshooting scenarios
- [AWS Error-Driven Troubleshooting Lab](https://github.com/charles-bucher/AWS_Error_Driven_Troubleshooting_Lab) - Error-driven learning labs

---

<div align="center">

**⭐ If this helped you learn CloudOps, please star it! ⭐**

Made with ☁️ by [Charles Bucher](https://github.com/charles-bucher)

</div>