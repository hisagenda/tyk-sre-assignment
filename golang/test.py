from kubernetes import client, config # \Python official Library: https://github.com/kubernetes-client/python/

# Configure Kubernetes connection (Use Defaut context)
config.load_kube_config()

# Create instances of AppsV1Api and CoreV1Api
apps_v1 = client.AppsV1Api()  # For deployment listing
core_v1 = client.CoreV1Api()  # For pod listing

# Get all deployments
deployments = apps_v1.list_deployment_for_all_namespaces(watch=False)

# Initialize a list to store the results
results = []

# Loop through deployments
for deployment in deployments.items:
    # Get desired replica count
    desired_replicas = deployment.spec.replicas

    # Get actual number of ready pods
    selector = deployment.spec.selector.match_labels
    pod_list = core_v1.list_namespaced_pod(
        namespace=deployment.metadata.namespace,
        label_selector=", ".join([f"{k}={v}" for k, v in selector.items()]))
    ready_pods = sum(1 for pod in pod_list.items if pod.status.phase == "Running")

    # Check if desired and actual numbers match
    if desired_replicas != ready_pods:
        result = f"[WARNING] Deployment {deployment.metadata.name}: Expected {desired_replicas} pods, but only {ready_pods} are ready."
    else:
        result = f"Deployment {deployment.metadata.name} is healthy: {desired_replicas} out of {ready_pods} desired replicas are ready."
    results.append(result)

# Print the results
if results:
    print("Deployments in the k8s cluster:")
    for result in results:
        print(result)
else:
    print("All deployments seem to have the desired number of healthy pods.")
