#!/bin/bash

# CREATE CONTAINERS

## Create the container for the GCP app deployment
#cd ~/edge-computing-foundations-architecting-applications-for-the-edge-2028253/GCP-Deployment/create
#docker build -t guestbook-gcp-app .
#docker tag guestbook-gcp-app us-central1-docker.pkg.dev/gdcedge/gdcc-course/guestbook-gcp-app:latest
#docker push us-central1-docker.pkg.dev/gdcedge/gdcc-course/guestbook-gcp-app:latest


# DEPLOY APPLICATION

## Deploy application to GCP
cd ~/edge-computing-foundations-architecting-applications-for-the-edge-2028253/GCP-Deployment/deploy
kubectl apply -f deployment.yaml
