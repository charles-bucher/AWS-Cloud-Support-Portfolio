AWS Cloud Support Simulator 🚀

Hands-on AWS Cloud Support portfolio focused on real troubleshooting, not tutorials.

Entry-level cloud engineer proving skills through real AWS infrastructure, intentional failures, systematic debugging, and professional documentation.

TL;DR (For Hiring Managers)

Target role: AWS Cloud Support Associate / Junior SysOps

What this repo is: A real AWS lab I built, broke, fixed, and documented

How it’s built: Terraform (reproducible, destroyable, safe for GitHub)

What it proves: I can troubleshoot cloud issues using logs, metrics, IAM, and CLI

Included Scenarios (Real Issues, Real Fixes)

EC2 SSH connectivity failures

S3 AccessDenied (IAM vs bucket policy)

Lambda timeouts & performance tuning

IAM policy syntax & permission errors

GuardDuty security findings & incident response

👉 Start here: /scenarios/ec2_connectivity.md

What This Project Is (Short Answer)

I’m not claiming experience — I’m building proof.

This repository shows:

Infrastructure I deployed in my own AWS account

Problems I intentionally created

How I investigated them

How I fixed them

Evidence (logs, metrics, screenshots, CLI output)

This mirrors real Cloud Support tickets, not classroom labs.

Why This Exists

I’m transitioning into cloud operations from non-tech work.
Instead of asking for chances, I’m showing exactly how I think, troubleshoot, and document issues.

This is not production infrastructure.
It is production-style troubleshooting.

Architecture Overview

Fully deployed via Terraform (rebuildable end-to-end).

AWS Region: us-east-1

Services Used

Compute: EC2, Lambda

Storage: S3, EBS

Networking: VPC, subnets, route tables, security groups

Security: IAM, GuardDuty, CloudTrail

Monitoring: CloudWatch Logs, Metrics, Alarms

I can destroy and rebuild this environment from scratch in minutes.

Lab Scenarios (Core of This Repo)

Each scenario follows the same structure:

Problem creation

Investigation (logs, metrics, CLI)

Root cause analysis

Fix

Validation + evidence

Scenario	AWS Services	Skills Practiced	Status
EC2 Connectivity	EC2, VPC, SGs	Network troubleshooting	✅
S3 Access Denied	S3, IAM	Permission debugging	✅
Lambda Timeout	Lambda, CloudWatch	Performance tuning	✅
IAM Errors	IAM, Logs	Policy troubleshooting	✅
GuardDuty Alerts	GuardDuty, CloudTrail	Incident response	✅

👉 Full walkthroughs live in /scenarios

Example: EC2 Connectivity Issue (Summary)

Problem:
EC2 instance unreachable via SSH.

Investigation:

Instance state verified

Security group rules reviewed

Route tables checked

VPC Flow Logs examined

Root Cause:
Missing inbound SSH rule in Security Group.

Fix:
Restricted SSH access to my IP only (best practice).

Result:

SSH successful

Issue resolved in ~12 minutes

📄 Full write-up: /scenarios/ec2_connectivity.md

Incident Response Example: GuardDuty

I intentionally triggered GuardDuty findings to practice security response.

Actions Taken

Reviewed finding severity

Traced activity via CloudTrail

Deactivated compromised IAM key

Rotated credentials

Tightened security groups

Enabled MFA

Documented incident & created runbook

This follows a calm, checklist-driven response, not guesswork.

Validation & Testing

Basic Python tests validate:

Connectivity assumptions

IAM permissions

Lambda execution success

These are operational sanity checks, not application unit tests — the kind Cloud Support uses to confirm fixes.

Project Structure
AWS_Cloud_Support_Sim/
├── iac/            # Terraform (VPC, EC2, IAM, Lambda, GuardDuty)
├── scenarios/      # Step-by-step troubleshooting walkthroughs
├── runbooks/       # Operational response guides
├── scripts/        # Automation & remediation
├── tests/          # Validation checks
├── diagrams/       # Architecture visuals
├── screenshots/    # Evidence from my AWS account
└── README.md

Quick Start (Reproducible Lab)

⚠️ Deploys real AWS resources (~$5–10/month if left running)

git clone https://github.com/charles-bucher/AWS_Cloud_Support_Sim.git
cd AWS_Cloud_Support_Sim/iac
terraform init
terraform plan
terraform apply


Destroy when finished:

terraform destroy

Skills Demonstrated (Honest Levels)
Skill	Level	Evidence
AWS Console & CLI	Comfortable	Screenshots + CLI output
EC2 Troubleshooting	Learning	Scenario 1
S3 Operations	Learning	Scenario 2
IAM Debugging	Basic–Intermediate	Scenarios 2 & 4
CloudWatch Logs	Basic	All scenarios
Lambda	Learning	Scenario 3
Terraform	Solid Beginner	Full environment
Linux/Bash	Comfortable	Daily usage
Git/GitHub	Comfortable	This repo
Documentation	Strong	Runbooks + RCAs
What I’m Learning Now

AWS Solutions Architect Associate (studying, no rush)

Auto Scaling Groups & Load Balancers

CloudFormation (comparison with Terraform)

Cost optimization patterns

Career Target

Roles

AWS Cloud Support Associate

Junior SysOps Administrator

Cloud Operations Engineer (Entry-level)

Preferences

Remote (US-based)

Open to contract or staffing agencies

Why This Repo Matters

No fake experience

No tutorial screenshots

No inflated titles

Everything here:

Ran in my AWS account

Cost my own money

Was built after long work shifts

Is fully inspectable

I can’t fake experience — so I built proof.

Contact

Charles Bucher
Self-Taught Cloud Engineer | Open to Work

GitHub: https://github.com/charles-bucher

Portfolio: https://charles-bucher.github.io

LinkedIn: https://linkedin.com/in/charles-bucher-cloud

Email: quietopscb@gmail.com