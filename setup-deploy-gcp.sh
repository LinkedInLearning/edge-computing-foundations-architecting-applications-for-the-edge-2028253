#!/bin/bash

# DEPLOY APPLICATION

## Deploy application to GCP
cd ~/edge-computing-foundations-architecting-applications-for-the-edge-2028253/GCP-Deployment/deploy
kubectl apply -f deployment.yaml

echo "deployment completed"
