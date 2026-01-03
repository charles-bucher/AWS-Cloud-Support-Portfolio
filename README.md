# AWS SysOps Administrator Lab Environment 🚀

<div align="center">

## 🎯 Self-Taught AWS Portfolio Project

[![AWS](https://img.shields.io/badge/AWS-Learning_SysOps-FF9900?style=for-the-badge&logo=amazon-aws&logoColor=white)](https://aws.amazon.com/)
[![Self-Study](https://img.shields.io/badge/Status-Self_Teaching-orange?style=for-the-badge&logo=amazon-aws&logoColor=white)](https://aws.amazon.com/)
[![Active Development](https://img.shields.io/badge/Project-Active_Development-brightgreen?style=for-the-badge)](https://github.com/charles-bucher/AWS_Cloud_Support_Sim)
[![Open to Work](https://img.shields.io/badge/Hiring-Entry_Level_Cloud-success?style=for-the-badge)](https://linkedin.com/in/charles-bucher-cloud)

**Building hands-on AWS skills through real-world scenarios**  
*Career transition to cloud operations*

</div>

---

## 🎓 My Learning Journey (Honest Status)

**Background:** Self-teaching AWS to transition into cloud operations  
**Current Role:** Part-time delivery driver while building cloud skills  
**Goal:** Entry-level AWS SysOps/Cloud Support role

### What I'm Actually Doing

```
✅ COMPLETED
├─ Deployed real AWS infrastructure (EC2, VPC, S3, Lambda)
├─ Built 5 troubleshooting scenarios with screenshots
├─ Learned Terraform for Infrastructure as Code
├─ Wrote Python automation scripts
└─ Documented everything professionally

🔄 CURRENTLY WORKING ON
├─ AWS Solutions Architect - Associate study
├─ Adding more complex scenarios (ASG, ELB)
├─ Learning CloudFormation
└─ Practicing for certification exam

📋 PLANNED NEXT
├─ Take AWS SAA exam when ready
├─ Build CI/CD pipeline project
├─ Learn container basics (ECS)
└─ Add monitoring/alerting scenarios
```

### Skills I've Built (No Exaggeration)

| Skill | Level | Evidence |
|-------|-------|----------|
| AWS Console Navigation | Comfortable | Screenshots throughout repo |
| EC2 Basics | Learning | Can launch/troubleshoot instances |
| S3 Operations | Learning | Bucket policies, access control |
| IAM Policies | Basic | Can read/modify policies |
| CloudWatch Logs | Basic | Can search logs, spot errors |
| Terraform | Beginner | Can deploy basic infrastructure |
| Python Scripts | Basic | Simple automation tasks |
| Linux/Bash | Comfortable | Daily use for projects |
| Git/GitHub | Comfortable | This repo proves it |
| Documentation | Strong | You're reading it |

**Translation for Employers:** I'm entry-level, but I can prove I've actually touched AWS and built things.

---

## 📋 Table of Contents

- [Why I Built This](#why-i-built-this)
- [What I've Actually Built](#what-ive-actually-built)
- [Architecture](#architecture)
- [Lab Scenarios](#lab-scenarios)
- [Quick Start](#quick-start)
- [What I'm Learning](#what-im-learning)
- [Career Goals](#career-goals)
- [Contact](#contact)

---

## 💡 Why I Built This

**Short Answer:** I need to prove I can do the work, not just say I'm "learning AWS."

**Long Answer:**  
I'm transitioning to cloud from delivery work. I have a record from 2003 (clean since 2008). I know I need to work twice as hard to get an interview.

So instead of just watching tutorials, I'm building a portfolio that shows:
- ✅ I can actually navigate AWS Console
- ✅ I can troubleshoot real problems
- ✅ I can document my work professionally
- ✅ I'm serious about this career change

### What Makes This Real

**Not Theory:**
- ❌ I didn't just copy someone's tutorial
- ❌ I didn't use sample screenshots from Google
- ❌ I didn't claim skills I don't have

**Actually Built:**
- ✅ Every screenshot is from MY AWS account
- ✅ I broke things on purpose to learn how to fix them
- ✅ I spent my own money on AWS (Free Tier + ~$20)
- ✅ I worked on this after 10-hour delivery shifts

---

## 🔧 What I've Actually Built

### Real Infrastructure I Deployed

**VPC Environment**
- Custom VPC with public/private subnets
- Internet Gateway and route tables
- Security Groups with proper rules
- Network ACLs for defense in depth

**Compute & Storage**
- EC2 instances (practiced SSH, security groups)
- S3 buckets (policies, encryption, versioning)
- Lambda functions (IAM roles, CloudWatch logs)

**Security & Monitoring**
- IAM roles and policies
- GuardDuty for threat detection
- CloudWatch for logs and metrics
- Practiced incident response workflow

**All deployed with Terraform** - not clicking around Console

---

## 🏗️ Architecture

### What My Lab Environment Looks Like

```
┌─────────────────────────────────────────────────────────────────┐
│                         AWS Cloud                                │
│                                                                   │
│  ┌──────────────┐        ┌──────────────┐       ┌─────────────┐│
│  │   VPC        │        │  CloudWatch  │       │   GuardDuty ││
│  │              │        │              │       │             ││
│  │  ┌────────┐  │        │  - Logs      │       │  - Alerts   ││
│  │  │  EC2   │  │───────▶│  - Metrics   │───────▶│  - Findings ││
│  │  │Instance│  │        │  - Alarms    │       │             ││
│  │  └────────┘  │        └──────────────┘       └─────────────┘│
│  │              │                                                │
│  │  ┌────────┐  │        ┌──────────────┐                       │
│  │  │  S3    │  │        │   Lambda     │                       │
│  │  │ Bucket │  │        │   Function   │                       │
│  │  └────────┘  │        └──────────────┘                       │
│  │              │                                                │
│  │  ┌────────┐  │                                                │
│  │  │  IAM   │  │        Deployed via Terraform                 │
│  │  │ Roles  │  │                                                │
│  │  └────────┘  │                                                │
│  └──────────────┘                                                │
└─────────────────────────────────────────────────────────────────┘
```

### Scenario Flow Example

```
┌─────────────┐      ┌──────────────┐      ┌─────────────┐      ┌──────────────┐
│   Alert     │─────▶│ Investigation│─────▶│  Root Cause │─────▶│  Remediation │
│  Received   │      │   & Logs     │      │   Analysis  │      │  & Testing   │
└─────────────┘      └──────────────┘      └─────────────┘      └──────────────┘
                            │                      │                     │
                            ▼                      ▼                     ▼
                     CloudWatch Logs        IAM Policy Issue      Updated Policy
                     Error Messages         Missing Permissions   Function Success
```

![VPC Architecture Setup](screenshots/01_vpc_architecture_setup.png)
*Figure 1: Complete VPC architecture I built with subnets, routing, and security groups*

![VPC Subnets and Routing](screenshots/02_vpc_subnets_routing.png)
*Figure 2: Detailed subnet configuration and route table associations*

### Lab Environment Status

![Lab Environment Verified](screenshots/00_lab_environment_verified.png)
*✅ Verified working lab environment I deployed via Terraform*

---

## 🔧 Lab Scenarios (What I've Learned)

Each scenario = a problem I created, investigated, and fixed. This is how I learn.

### 1️⃣ EC2 Connectivity Issues

**What I Learned:** How to troubleshoot SSH connectivity

**Problem I Created:** Launched EC2 without proper Security Group rules  
**Investigation:**
- Checked Security Group (port 22 was blocked)
- Verified instance had public IP
- Confirmed route table had IGW route
- Learned to read VPC Flow Logs

**How I Fixed It:**
```bash
# Added inbound rule for SSH (port 22)
# Source: My IP (learned not to use 0.0.0.0/0 in production)
```

**Result:** ✅ Successfully connected via SSH

```
📊 BEFORE → AFTER
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Security Group Rules:
❌ BEFORE: Port 22 - No inbound rule
✅ AFTER:  Port 22 - My IP only (secure!)

Connection Status:
❌ BEFORE: ssh: connect to host timeout
✅ AFTER:  Successfully authenticated
```

![Security Groups Configuration](screenshots/03_security_groups_network_acls.png)
*Figure 3: Security Group rules I configured after learning my mistake*

**Key Learning:** Always check Security Groups first. Saves hours of troubleshooting.

---

### 2️⃣ S3 Access Denied Errors

**What I Learned:** IAM policies control S3 access, not just bucket policies

**Problem I Created:** EC2 instance couldn't access S3 bucket  
**Investigation:**
- Checked S3 bucket policy (looked fine)
- Checked IAM role attached to EC2 (missing permissions!)
- Learned the difference between resource policies and identity policies
- Analyzed CloudWatch logs to confirm AccessDenied errors

**How I Fixed It:**
```json
{
  "Effect": "Allow",
  "Action": ["s3:GetObject", "s3:PutObject"],
  "Resource": "arn:aws:s3:::my-bucket/*"
}
```

**Result:** ✅ Application successfully reading/writing to S3

```
📊 BEFORE → AFTER
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
IAM Policy:
❌ BEFORE: No S3 permissions on EC2 role
✅ AFTER:  s3:GetObject, s3:PutObject allowed

Application Logs:
❌ BEFORE: AccessDenied (403) error
✅ AFTER:  Objects retrieved successfully (200 OK)
```

![S3 Bucket Setup](screenshots/06_s3_bucket_setup.png)
*Initial S3 bucket creation and configuration*

![S3 Bucket Configuration](screenshots/08_s3_bucket_configuration.png)
*Figure 4: S3 bucket permissions and IAM policy I configured*

**Key Learning:** IAM is confusing at first, but it's just "who can do what to which resources."

---

### 3️⃣ Lambda Function Timeout

**What I Learned:** Lambda has limits, and you need to configure them properly

**Problem I Created:** Lambda function timing out at default 3 seconds  
**Investigation:**
- Checked CloudWatch Logs (saw timeout errors)
- Analyzed execution duration metrics
- Learned about Lambda memory/timeout limits
- Discovered my code was inefficient

**How I Fixed It:**
- Increased timeout from 3s to 30s
- Optimized code (learned about connection pooling)
- Added error handling

**Result:** ✅ Function completing in < 5 seconds

```
📊 BEFORE → AFTER
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Lambda Configuration:
❌ BEFORE: Timeout: 3 seconds (default)
✅ AFTER:  Timeout: 30 seconds

CloudWatch Metrics:
❌ BEFORE: Duration: 3000ms (always timeout)
✅ AFTER:  Duration: 4200ms (success)

Error Rate:
❌ BEFORE: 95% timeout errors
✅ AFTER:  0% errors, 100% success rate
```

![CloudWatch Monitoring Dashboard](screenshots/09_cloudwatch_monitoring_dashboard.png)
*Figure 5: CloudWatch metrics showing my Lambda function after I fixed it*

**Key Learning:** Always check CloudWatch Logs first. They tell you exactly what's wrong.

---

### 4️⃣ IAM Permission Errors

**What I Learned:** IAM policies are picky about syntax

**Problem I Created:** Service couldn't write logs to CloudWatch  
**Investigation:**
- Reviewed IAM policy (looked right to me at first)
- Checked trust relationship (was correct)
- Learned that resource ARNs matter
- Finally found the issue: wrong resource format

**How I Fixed It:**
```json
{
  "Effect": "Allow",
  "Action": [
    "logs:CreateLogGroup",
    "logs:CreateLogStream",
    "logs:PutLogEvents"
  ],
  "Resource": "arn:aws:logs:*:*:*"
}
```

**Result:** ✅ Logs flowing to CloudWatch successfully

```
📊 BEFORE → AFTER
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
IAM Policy Permissions:
❌ BEFORE: Missing CloudWatch Logs actions
✅ AFTER:  All 3 required actions added

CloudWatch Log Groups:
❌ BEFORE: No logs appearing (silent failure)
✅ AFTER:  Log stream active, events flowing

Error Messages:
❌ BEFORE: AccessDeniedException
✅ AFTER:  Logs successfully written
```

![IAM Roles and Policies](screenshots/04_iam_roles_policies_setup.png)
*Figure 6: IAM role I configured after learning how CloudWatch Logs permissions work*

**Key Learning:** IAM errors are frustrating but teach you to read documentation carefully.

---

### 5️⃣ GuardDuty Security Findings

**What I Learned:** How to respond to security alerts (incident response basics)

**Problem I Created:** Intentionally triggered GuardDuty alerts to practice  
**Investigation:**
- Reviewed GuardDuty findings dashboard
- Checked CloudTrail logs for suspicious activity
- Identified which access key was "compromised"
- Learned to trace API calls back to source

**How I Fixed It:**
1. Rotated the IAM access key immediately
2. Updated Security Group rules (too permissive)
3. Enabled MFA on root account (should've done this first!)
4. Configured SNS alerts for future findings

**Result:** ✅ Security posture improved, practiced incident response

```
📊 INCIDENT RESPONSE TIMELINE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Detection:
  GuardDuty Finding: UnauthorizedAccess (simulated)

Investigation (CloudTrail):
  - Identified which access key was "compromised"
  - Traced API calls to find affected resources
  - Learned to read CloudTrail JSON

Remediation Actions I Took:
  ✅ Rotated IAM access keys
  ✅ Tightened Security Group rules
  ✅ Enabled MFA (finally!)
  ✅ Set up SNS alerts for future issues

Validation:
  ✅ No further unauthorized access
  ✅ GuardDuty findings archived
  ✅ Monitoring now alerts me via email
```

![GuardDuty Dashboard](screenshots/07_guardduty_dashboard_overview.png)
*Figure 7: GuardDuty findings I practiced responding to*

**Key Learning:** Security incidents are scary at first, but there's a methodical process to follow.

---

## 📊 Development Workflow

I'm learning professional development practices too:

![Git Branch and Merge Workflow](screenshots/05_git_branch_merge_workflow.png)
*Learning to use git properly: branches, commits, pull requests*

**What I Practice:**
- ✅ Feature branches (not committing directly to main)
- ✅ Meaningful commit messages
- ✅ Testing before merging
- ✅ Keeping my repo organized

**Why This Matters:** Real DevOps/SysOps jobs require good git habits.

---

## 🚀 Quick Start

**Warning:** This will create AWS resources. Use Free Tier or expect small charges (~$5).

### Prerequisites
- AWS Account (Free Tier works)
- AWS CLI configured with your credentials
- Terraform installed
- Basic Linux/terminal knowledge

### Deploy My Lab Environment

```bash
# Clone repository
git clone https://github.com/charles-bucher/AWS_Cloud_Support_Sim.git
cd AWS_Cloud_Support_Sim

# Initialize Terraform
terraform init

# See what will be created
terraform plan

# Deploy the lab (creates real AWS resources)
terraform apply -auto-approve

# When done, destroy to avoid charges
terraform destroy -auto-approve
```

---

## 📁 Project Structure

```
AWS_Cloud_Support_Sim/
├── iac/                      # Infrastructure as Code
│   ├── main.tf              # Core Terraform config
│   ├── variables.tf         # Variables
│   ├── outputs.tf           # Outputs
│   ├── s3_security.tf       # S3 configurations
│   └── sg_hardening.tf      # Security Groups
├── scenarios/                # Learning scenarios
│   ├── ec2_connectivity.md
│   ├── s3_access_denied.md
│   ├── lambda_timeout.md
│   ├── iam_permissions.md
│   └── guardduty_alerts.md
├── scripts/                  # Automation scripts
│   ├── simulate_errors.py
│   ├── remediation.py
│   └── monitoring_setup.py
├── screenshots/              # Proof of work
├── diagrams/                 # Architecture diagrams
└── README.md                 # You are here
```

---

## 🛠️ Technologies I'm Learning

### Cloud Platform
![AWS](https://img.shields.io/badge/Amazon_AWS-FF9900?style=for-the-badge&logo=amazonaws&logoColor=white)

**Services I've Used:**
- EC2, VPC, S3, Lambda, IAM, CloudWatch, GuardDuty

### Infrastructure & Automation
![Terraform](https://img.shields.io/badge/Terraform-7B42BC?style=for-the-badge&logo=terraform&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Bash](https://img.shields.io/badge/Bash-4EAA25?style=for-the-badge&logo=gnu-bash&logoColor=white)

### Tools I Use
![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white)
![VS Code](https://img.shields.io/badge/VS_Code-007ACC?style=for-the-badge&logo=visual-studio-code&logoColor=white)
![Linux](https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black)

---

## 📚 What I'm Currently Learning

### Active Study (January 2025)

**AWS Solutions Architect - Associate**
- Studying for exam (no date scheduled yet)
- Following Stephane Maarek's Udemy course
- Doing hands-on labs from Tutorials Dojo
- Building this project to reinforce learning

**Next Skills:**
- CloudFormation
- Auto Scaling Groups and Load Balancers
- Container basics (ECS)
- CI/CD pipelines

### Resources I Use

**Free:**
- AWS Free Tier
- AWS Documentation
- YouTube tutorials
- Reddit r/AWSCertifications

**Paid:**
- Udemy courses ($10-15)
- Tutorials Dojo practice exams ($15)
- AWS account costs (~$20/month)

---

## 🎯 Career Goals (Realistic)

### What I'm Looking For

**Target Roles:**
- AWS Cloud Support Associate
- Junior SysOps Administrator
- Cloud Operations Engineer (Entry-level)
- Technical Support Engineer (Cloud)

**Salary Goals:**
- Year 1: $50k+ (entry-level)
- Years 2-3: $70-90k combined household
- Years 4-5: $100k individual

**Location:**
- Remote preferred (Florida-based)
- Open to contract/staffing agencies
- Will consider hybrid if Tampa Bay area

### Why Hire Me?

**What I Bring:**
- ✅ Actual hands-on AWS experience (this repo proves it)
- ✅ Self-motivated (taught myself while working full-time)
- ✅ Documentation skills (professional docs)
- ✅ Problem-solving mindset
- ✅ Humble and willing to learn

**What I Need:**
- ✅ Chance to prove myself
- ✅ Remote opportunity
- ✅ Entry-level role
- ✅ Company that values skills over credentials

---

## 📞 Contact

**Charles Bucher**

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com/in/charles-bucher-cloud)
[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Charles-Bucher)
[![Email](https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:charles.bucher.cloud@gmail.com)

**Status:** Open to entry-level cloud opportunities (remote preferred)

**Looking For:**
- AWS Cloud Support roles
- Junior SysOps positions
- Contract work through staffing agencies
- Freelance AWS projects

---

## 📄 License

MIT License - see [LICENSE.md](LICENSE.md)

---

## 🙏 The Truth

**I'm Self-Taught:**
- This is a learning project, not production work
- I'm entry-level, not senior
- I have a record from 2003 (clean since 2008)
- I'm 40 with three kids, no time for BS

**But Here's What's Real:**
- Every screenshot is from MY AWS account
- I spent MY money learning
- I built this after MY delivery shifts
- This is MY actual learning journey

**Bottom Line:** I can't fake experience, so I'm building proof.

---

<div align="center">

**⭐ If you find this helpful, please star this repo**

Built with ☕ and determination

**Charles Bucher**  
*Self-Taught Cloud Engineer*

</div>