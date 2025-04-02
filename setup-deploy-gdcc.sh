#!/bin/bash

# CREATE CONTAINERS

## Create the container for the GDCC app deployment
#cd ~/edge-computing-foundations-architecting-applications-for-the-edge-2028253/GDCC-Deployment/create
#docker build -t guestbook-gdcc-app .
#docker tag guestbook-gdcc-app us-central1-docker.pkg.dev/gdcedge/gdcc-course/guestbook-gdcc-app:latest
#docker push us-central1-docker.pkg.dev/gdcedge/gdcc-course/guestbook-gdcc-app:latest



# DEPLOY APPLICATION

## Deploy application to GDCC
cd ~/edge-computing-foundations-architecting-applications-for-the-edge-2028253/GDCC-Deployment/deploy
kubectl apply -f postgres-configmap.yaml
kubectl apply -f postgres-db-deployment.yaml
kubectl apply -f deployment.yaml
