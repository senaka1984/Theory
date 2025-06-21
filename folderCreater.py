import os

# List of folder names to create
folder_names = [
    "01. DevOps Fundamentals",
    "02. Source Control Management",
    "03. Continuous Integration CI Basics",
    "04. Build Tools",
    "05. Cloud and Infrastructure Basics",
    "06. Configuration Management",
    "07. Continuous Deployment CD",
    "08. Infrastructure as Code IaC",
    "09. Containerization AND Orchestration",
    "10. Monitoring & Logging",
    "11. Security Practices DevSecOps",
    "12. Site Reliability Engineering SRE",
    "13. Advanced CICD Strategies",
    "14. Cost and Performance Optimization",
    "15. Policy as Code AND Compliance",
    "16. Multi-cloud and Hybrid Strategies",
    "17. Platform Engineering & Internal Developer Platforms IDP"
]

# Parent directory where folders will be created
parent_dir = "E:/Theory/08. DevOps"

# Create each folder
for name in folder_names:
    path = os.path.join(parent_dir, name)
    try:
        os.makedirs(path, exist_ok=True)
        print(f"Created: {path}")
    except Exception as e:
        print(f"Error creating {path}: {e}")