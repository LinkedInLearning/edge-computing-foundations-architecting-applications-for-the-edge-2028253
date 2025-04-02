#!/bin/bash

# DEPLOY APPLICATION

## Deploy application to GDCC
cd ~/edge-computing-foundations-architecting-applications-for-the-edge-2028253/GDCC-Deployment/deploy
kubectl apply -f postgres-configmap.yaml
kubectl apply -f postgres-db-deployment.yaml
kubectl apply -f deployment.yaml

echo "deployment completed"
