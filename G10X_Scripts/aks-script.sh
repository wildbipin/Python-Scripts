#!/bin/bash

# Set the variables as requirement

# TENANT_ID = 'ebc8e959-fe38-4731-b824-063810e0b9eb'
# SUBSCRIPTION_ID = '10ba76d4-ba03-464a-ace0-10fa2efdbf0c'
RESOURCE_GROUP="myResourceGroup"
CLUSTER_NAME="myAKSCluster"
NODE_COUNT=4
NODE_SIZE="Standard_B2s"
LOCATION="centralindia" # You can change this to your desired Azure region

# Create a resource group
az group create --name $RESOURCE_GROUP --location $LOCATION

# Create the AKS cluster
az aks create \
    --resource-group $RESOURCE_GROUP \
    --name $CLUSTER_NAME \
    --node-count $NODE_COUNT \
    --node-vm-size $NODE_SIZE \
    --enable-addons http_application_routing \
    --generate-ssh-keys

# Get the credentials for the AKS cluster to connect with AKS cluster using kubectl CLI
az aks get-credentials --resource-group $RESOURCE_GROUP --name $CLUSTER_NAME

# # Verify your connection to cluster
# kubectl get nodes
