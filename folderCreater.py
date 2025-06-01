import os

# List of folder names to create
folder_names = [
    "01. Docker basics: images, containers, volumes",
    "02. Azure Container Registry AWS ECR",
    "03. Azure Kubernetes Service (AKS) Amazon EKS",
    "04. Deployments, Services, ConfigMaps, Secrets",
    "05. Helm Charts",
    "06. Horizontal Pod Autoscaler",
    "07. CICD for containers (GitHub Actions, Azure DevOps Pipelines)",
    "08. Secure container images and scanning",
    "09. Observability in Kubernetes (Prometheus, Grafana, etc.)"

]

# Parent directory where folders will be created
parent_dir = "E:/Theory/05. Basics/07. Cloud/09 📦 Containers and Kubernetes in the Cloud"

# Create each folder
for name in folder_names:
    path = os.path.join(parent_dir, name)
    try:
        os.makedirs(path, exist_ok=True)
        print(f"Created: {path}")
    except Exception as e:
        print(f"Error creating {path}: {e}")