# Tyk Assignment Go

This README provides instructions for deploying, and running the Tyk Assignment Go application using Docker and Helm.

Helm Chart Creation and Deployment

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
