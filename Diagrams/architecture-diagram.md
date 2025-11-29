graph TB
    subgraph "AWS Cloud"
        subgraph "Monitoring & Observability"
            CW[CloudWatch Metrics & Logs]
            LA[Lambda Functions]
            SNS[SNS Topics]
        end
        
        subgraph "Security"
            GD[GuardDuty]
            SH[Security Hub]
            IAM[IAM Policies]
        end
        
        subgraph "Infrastructure"
            EC2[EC2 Instances]
            S3[S3 Buckets]
            VPC[VPC & Subnets]
        end
        
        subgraph "IaC Tools"
            TF[Terraform]
            CF[CloudFormation]
        end
    end
    
    subgraph "Automation"
        PY[Python Scripts]
        CI[CI/CD Pipeline]
    end
    
    EC2 --> CW
    S3 --> CW
    CW --> LA
    LA --> SNS
    SNS --> |Alerts| EMAIL[Email Notifications]
    
    GD --> SH
    SH --> LA
    
    TF --> EC2
    TF --> S3
    TF --> VPC
    CF --> IAM
    
    PY --> LA
    CI --> TF
    CI --> CF
    
    style CW fill:#FF9900
    style LA fill:#FF9900
    style SNS fill:#FF9900
    style GD fill:#DD344C
    style TF fill:#7B42BC
    style PY fill:#3776AB