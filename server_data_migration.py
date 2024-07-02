import paramiko
from scp import SCPClient

def create_ssh_client(server, port, user, password):
    """Create an SSH client and connect to the server."""
    client = paramiko.SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(server, port, user, password)
    return client

def copy_files_via_scp(ssh_client, remote_path, local_path):
    """Copy files from remote server to local path using SCP."""
    with SCPClient(ssh_client.get_transport()) as scp:
        scp.get(remote_path, local_path)

def upload_files_via_scp(ssh_client, local_path, remote_path):
    """Upload files from local path to remote server using SCP."""
    with SCPClient(ssh_client.get_transport()) as scp:
        scp.put(local_path, remote_path)

def main():
    # Source server details
    src_server = 'source_server_ip'
    src_port = 22
    src_user = 'source_username'
    src_password = 'source_password'
    src_path = '/path/to/source/data/*'

    # Destination server details
    dest_server = 'destination_server_ip'
    dest_port = 22
    dest_user = 'destination_username'
    dest_password = 'destination_password'
    dest_path = '/path/to/destination/data/'

    # Local temporary storage path
    local_path = '/path/to/local/temp/'

    # Create SSH clients for source and destination servers
    src_ssh_client = create_ssh_client(src_server, src_port, src_user, src_password)
    dest_ssh_client = create_ssh_client(dest_server, dest_port, dest_user, dest_password)

    try:
        # Step 1: Copy files from source server to local machine
        print(f"Copying files from {src_server}:{src_path} to local path {local_path}")
        copy_files_via_scp(src_ssh_client, src_path, local_path)

        # Step 2: Upload files from local machine to destination server
        print(f"Uploading files from local path {local_path} to {dest_server}:{dest_path}")
        upload_files_via_scp(dest_ssh_client, local_path, dest_path)

        print("Data migration completed successfully.")
    except Exception as e:
        print(f"Error occurred during data migration: {e}")
    finally:
        # Close SSH connections
        src_ssh_client.close()
        dest_ssh_client.close()

if __name__ == '__main__':
    main()