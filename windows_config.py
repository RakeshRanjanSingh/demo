import platform
import psutil

# Function to get Windows configuration
def get_windows_config():
    config = {}

    # General info
    config['platform'] = platform.system()
    config['platform_version'] = platform.version()
    config['architecture'] = platform.machine()
    config['hostname'] = platform.node()
    config['processor'] = platform.processor()

    # CPU info
    config['cpu_count'] = psutil.cpu_count(logical=False)
    config['cpu_threads'] = psutil.cpu_count(logical=True)
    config['cpu_frequency'] = psutil.cpu_freq().current

    # Memory info
    memory = psutil.virtual_memory()
    config['memory_total'] = memory.total / (1024 ** 3)  # GB
    config['memory_available'] = memory.available / (1024 ** 3)  # GB
    config['memory_used'] = memory.used / (1024 ** 3)  # GB
    config['memory_percent'] = memory.percent

    # Disk info
    disk = psutil.disk_usage('C:')
    config['disk_total'] = disk.total / (1024 ** 3)  # GB
    config['disk_used'] = disk.used / (1024 ** 3)  # GB
    config['disk_free'] = disk.free / (1024 ** 3)  # GB
    config['disk_percent'] = disk.percent

    return config

# Function to print Windows configuration
def print_windows_config(config):
    print(f"**General Information**")
    print(f"Platform: {config['platform']}")
    print(f"Platform Version: {config['platform_version']}")
    print(f"Architecture: {config['architecture']}")
    print(f"Hostname: {config['hostname']}")
    print(f"Processor: {config['processor']}")

    print(f"\n**CPU Information**")
    print(f"CPU Count (Physical): {config['cpu_count']}")
    print(f"CPU Threads (Logical): {config['cpu_threads']}")
    print(f"CPU Frequency: {config['cpu_frequency']} MHz")

    print(f"\n**Memory Information**")
    print(f"Total Memory: {config['memory_total']:.2f} GB")
    print(f"Available Memory: {config['memory_available']:.2f} GB")
    print(f"Used Memory: {config['memory_used']:.2f} GB")
    print(f"Memory Usage: {config['memory_percent']}%")

    print(f"\n**Disk Information (C:)**")
    print(f"Total Disk Space: {config['disk_total']:.2f} GB")
    print(f"Used Disk Space: {config['disk_used']:.2f} GB")
    print(f"Free Disk Space: {config['disk_free']:.2f} GB")
    print(f"Disk Usage: {config['disk_percent']}%")

# Main function
if __name__ == "__main__":
    config = get_windows_config()
    print_windows_config(config)
