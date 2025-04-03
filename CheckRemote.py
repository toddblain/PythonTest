import paramiko
import time

def check_process_remote(hostname, username, password, process_name):
    """
    Checks if a process is running on a remote server.

    Args:
        hostname (str): The hostname or IP address of the remote server.
        username (str): The username for SSH authentication.
        password (str): The password for SSH authentication.
        process_name (str): The name of the process to check.

    Returns:
        bool: True if the process is running, False otherwise.
    """
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        client.connect(hostname, username=username, password=password, timeout=10)
        command = f"ps -C {process_name} -o pid="
        stdin, stdout, stderr = client.exec_command(command)
        output = stdout.read().decode().strip()
        return bool(output)
    except Exception as e:
        print(f"Error: {e}")
        return False
    finally:
        client.close()

if __name__ == "__main__":
    hostname = "your_remote_host"
    username = "your_username"
    password = "your_password"
    process_name = "your_process_name"

    if check_process_remote(hostname, username, password, process_name):
        print(f"Process '{process_name}' is running on {hostname}.")
    else:
        print(f"Process '{process_name}' is not running on {hostname}.")

    # Example to check multiple processes
    processes_to_check = ["process1", "process2", "process3"]
    for process in processes_to_check:
        if check_process_remote(hostname, username, password, process):
            print(f"Process '{process}' is running on {hostname}.")
        else:
            print(f"Process '{process}' is not running on {hostname}.")
        time.sleep(1) # Add a delay to avoid overwhelming the server