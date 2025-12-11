# Define scenarios
$scenarios = @(
    "ec2-troubleshoot",
    "lambda-error",
    "s3-iam-access",
    "vpc-architecture",
    "security-groups-nacl",
    "cloudwatch-monitoring",
    "iam-role-policy",
    "guardduty-automation"
)

# Define files
$files = @("cloudformation.yaml", "{scenario}.txt", "instructions.md")

# Base folder
$baseDir = "scenarios"

# Create base folder if it doesn't exist
if (-Not (Test-Path $baseDir)) {
    New-Item -ItemType Directory -Path $baseDir
}

foreach ($scenario in $scenarios) {
    $scenarioDir = Join-Path $baseDir $scenario
    if (-Not (Test-Path $scenarioDir)) {
        New-Item -ItemType Directory -Path $scenarioDir
    }

    foreach ($file in $files) {
        $filename = $file -replace "{scenario}", $scenario
        $filepath = Join-Path $scenarioDir $filename

        if (-Not (Test-Path $filepath)) {
            # Create file with starter content
            switch -Wildcard ($filename) {
                "*.yaml" {
                    "# CloudFormation template for $scenario scenario" | Out-File -FilePath $filepath -Encoding UTF8
                }
                "*.txt" {
                    "# Troubleshooting steps for $scenario scenario" | Out-File -FilePath $filepath -Encoding UTF8
                }
                "*.md" {
                    "# Instructions for $scenario scenario" | Out-File -FilePath $filepath -Encoding UTF8
                }
            }
        }
    }
}

Write-Output "Folder structure and starter files created successfully!"
