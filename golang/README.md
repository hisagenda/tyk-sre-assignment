# Tyk Assignment Go

This README provides instructions for deploying, and running the Tyk Assignment Go application using Docker and Helm.


# DockerFile


A dockerfile is created in directory /golang and built then pushed using: 
docker build -t tyk-assignment-go .
docker tag tyk-assignment-go your-abiola89/tyk-assignment-go (For my public repository named abiola89)
docker push abiola89/tyk-assignment-go


# Helm Chart Creation and Deployment

1. Create a Helm chart for the application:
helm create tyk-assignment-go
2. Install the Helm chart:
helm install tyk-assignment-go ./tyk-assignment-go

## Helm Deployment Information

Upon successful deployment using Helm, you should see output similar to the following:
NAME: tyk-assignment-go
LAST DEPLOYED: Sun Feb 25 03:02:34 2024
NAMESPACE: default
STATUS: deployed
REVISION: 1
NOTES: 

### 


**Continuation:**

## Testing Kubernetes Deployments

To ensure the reliability and health of deployments in the Kubernetes cluster, a Python script named `test.py` has been added. This script utilizes the Kubernetes Python client library to query the cluster and verify whether the deployments have the expected number of healthy pods.

### Test Script Overview:

The `test.py` script performs the following steps:

1. **Configure Kubernetes Connection:** It loads the Kubernetes configuration to establish a connection to the cluster.

2. **Retrieve Deployment Information:** Using the Kubernetes client APIs, the script retrieves information about deployments across all namespaces.

3. **Check Replica Status:** For each deployment, it compares the desired replica count specified in the deployment configuration with the actual number of ready pods. If the counts match, the deployment is considered healthy; otherwise, a warning message is generated.

### Running the Test:

To execute the test script, ensure you have the Kubernetes Python client library installed (`pip install kubernetes`) and configured properly. Then run the script using:

```bash
python test.py
```

### Example Output:

Upon execution, the script provides detailed information about the health status of deployments in the Kubernetes cluster. This includes whether deployments have the expected number of healthy pods or if any warnings are encountered.

We can proactively monitor and ensure the stability of our Kubernetes deployments


## Applying the Network Policy:
To apply the deny-all-traffic Network Policy, you can use the kubectl apply command with the YAML configuration provided above:

``kubectl apply -f deny-all-traffic.yaml``