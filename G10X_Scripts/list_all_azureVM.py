# # from azure.identity import DefaultAzureCredential

# # from azure.mgmt.compute import ComputeManagementClient

# # """
# # # PREREQUISITES
# #     pip install azure-identity
# #     pip install azure-mgmt-compute
# # # USAGE
# #     python virtual_machine_list_all_maximum_set_gen.py

# #     Before run the sample, please set the values of the client ID, tenant ID and client secret
# #     of the AAD application as environment variables: AZURE_CLIENT_ID, AZURE_TENANT_ID,
# #     AZURE_CLIENT_SECRET. For more info about how to get the value, please see:
# #     https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal
# # """


# # def main():
# #     client = ComputeManagementClient(
# #         credential=DefaultAzureCredential(),
# #         subscription_id="10ba76d4-ba03-464a-ace0-10fa2efdbf0c",
# #     )

# #     response = client.virtual_machines.list_all()
# #     for item in response:
# #         print(item)


# # # x-ms-original-file: specification/compute/resource-manager/Microsoft.Compute/ComputeRP/stable/2024-03-01/examples/virtualMachineExamples/VirtualMachine_ListAll_MaximumSet_Gen.json
# # if __name__ == "__main__":
# #     main()

import requests
import json

# Azure credentials
tenant_id = '$xxx'
client_id = '$yyy'
client_secret = '$zzz'
subscription_id = '$aaa'
resource_group = '$bbb'

# Azure endpoints
auth_url = f'https://login.microsoftonline.com/{tenant_id}/oauth2/token'
vm_list_url = f'https://management.azure.com/subscriptions/{subscription_id}/resourceGroups/{resource_group}/providers/Microsoft.Compute/virtualMachines?api-version=2024-03-01'
# Get access token
def get_access_token(tenant_id, client_id, client_secret):
    payload = {
        'grant_type': 'client_credentials',
        'client_id': client_id,
        'client_secret': client_secret,
        'resource': 'https://management.azure.com/'
    }
    response = requests.post(auth_url, data=payload)
    response.raise_for_status()
    return response.json()['access_token']

# List VMs in the specified resource group
# def list_vms(access_token, vm_list_url):
#     headers = {
#         'Authorization': f'Bearer {access_token}',
#         'Content-Type': 'application/json'
#     }
#     response = requests.get(vm_list_url, headers=headers)
#     response.raise_for_status()
#     return response.json()

def main():
    # Obtain access token
    token = get_access_token(tenant_id, client_id, client_secret)
    
    # List VMs
    # vms = list_vms(token, vm_list_url)
    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json'
    }
    response = requests.get(vm_list_url, headers)
    response.raise_for_status()
    return response.json()
    
    # Print VM details
    for vm in vms.get('value', []):
        print(f"VM Name: {vm['name']}")
        print(f"VM ID: {vm['id']}")
        print(f"VM Location: {vm['location']}")
        print("-----------")

if __name__ == "__main__":
    main()



# import requests
# import json
# import logging

# # Configure logging
# logging.basicConfig(level=logging.DEBUG)

# # Azure AD credentials
# # tenant_id = 'your_tenant_id'
# # client_id = 'your_client_id'
# # client_secret = 'your_client_secret'
# # subscription_id = 'your_subscription_id'
# # resource_group = 'your_resource_group'

# # Authenticate and get the access token
# url = f"https://login.microsoftonline.com/{tenant_id}/oauth2/v2.0/token"
# payload = {
#     'grant_type': 'client_credentials',
#     'client_id': client_id,
#     'client_secret': client_secret,
#     'scope': 'https://management.azure.com/.default'
# }

# logging.debug(f"Requesting access token from {url}")
# response = requests.post(url, data=payload)
# logging.debug(f"Token request response: {response.status_code}, {response.text}")
# response.raise_for_status()
# access_token = response.json().get('access_token')

# if not access_token:
#     raise Exception("Failed to obtain access token")

# # Use the access token to list VMs in the specified resource group
# vm_url = f"https://management.azure.com/subscriptions/{subscription_id}/resourceGroups/{resource_group}/providers/Microsoft.Compute/virtualMachines?api-version=2021-07-01"
# headers = {
#     'Authorization': f'Bearer {access_token}',
#     'Content-Type': 'application/json'
# }

# logging.debug(f"Listing VMs with URL: {vm_url}")
# vm_response = requests.get(vm_url, headers=headers)
# logging.debug(f"VM listing response: {vm_response.status_code}, {vm_response.text}")

# if vm_response.status_code == 403:
#     logging.error("Access denied. Please check your role assignments and API permissions.")
#     raise Exception("403 Forbidden - Check your role assignments and API permissions")

# vm_response.raise_for_status()
# vms = vm_response.json()

# # Output the list of VMs
# print("List of VMs in resource group:")
# for vm in vms.get('value', []):
#     print(vm['name'])
