import psutil

def check_cpu():
    cpu_usage = psutil.cpu_percent(interval=1)
    print(f"CPU Usage: {cpu_usage}%")
    return cpu_usage

def check_memory():
    memory_info = psutil.virtual_memory()
    print(f"Memory Usage: {memory_info.percent}%")
    print(f"Total Memory: {memory_info.total / (1024 ** 3):.2f} GB")
    print(f"Available Memory: {memory_info.available / (1024 ** 3):.2f} GB")
    return memory_info.percent

def check_disk():
    disk_info = psutil.disk_usage('/')
    print(f"Disk Usage: {disk_info.percent}%")
    print(f"Total Disk Space: {disk_info.total / (1024 ** 3):.2f} GB")
    print(f"Used Disk Space: {disk_info.used / (1024 ** 3):.2f} GB")
    print(f"Free Disk Space: {disk_info.free / (1024 ** 3):.2f} GB")
    return disk_info.percent

def check_network():
    network_info = psutil.net_io_counters()
    print(f"Bytes Sent: {network_info.bytes_sent / (1024 ** 2):.2f} MB")
    print(f"Bytes Received: {network_info.bytes_recv / (1024 ** 2):.2f} MB")
    return network_info.bytes_sent, network_info.bytes_recv

if __name__ == "__main__":
    print("System Health Check:")
    cpu = check_cpu()
    memory = check_memory()
    disk = check_disk()
    network_sent, network_recv = check_network()

    # Add logic to alert if any of the metrics exceed threshold
    if cpu > 80:
        print("Warning: High CPU usage!")
    if memory > 80:
        print("Warning: High memory usage!")
    if disk > 90:
        print("Warning: High disk usage!")