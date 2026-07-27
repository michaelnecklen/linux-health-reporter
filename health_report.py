from datetime import timedelta
from pathlib import Path
import platform
import shutil
import socket

def get_uptime():
    uptime_text = Path("/proc/uptime").read_text()
    uptime_seconds = float(uptime_text.split()[0])
    return timedelta(seconds=int(uptime_seconds))


def bytes_to_gib(byte_count):
    return byte_count / (1024 ** 3)


def get_disk_status(percent_used):
    if not 0 <= percent_used <= 100:
        raise ValueError("percent_used must be between 0 and 100")
    if percent_used >= 90:
        return "CRITICAL"
    elif percent_used >= 80:
        return "WARNING"
    else:
        return "OK"


def main():
    hostname = socket.gethostname()
    kernel_version = platform.release()
    python_version = platform.python_version()
    uptime = get_uptime()
    disk = shutil.disk_usage("/")
    disk_total = bytes_to_gib(disk.total)
    disk_used = bytes_to_gib(disk.used)
    disk_available = bytes_to_gib(disk.free)
    disk_percent = disk.used / (disk.used + disk.free) * 100
    disk_status = get_disk_status(disk_percent)

    print("Linux System Health Report")
    print("==========================")
    print(f"Hostname:  {hostname}")
    print(f"Kernel:    {kernel_version}")
    print(f"Python:    {python_version}")
    print(f"Uptime:    {uptime}")
    print()
    print("Root Filesystem")
    print("---------------")
    print(f"Total:        {disk_total:.1f} GiB")
    print(f"Used:         {disk_used:.1f} GiB")
    print(f"Available:    {disk_available:.1f} GiB")
    print(f"Utilized:     {disk_percent:.1f}%")
    print(f"Status:       {disk_status}")


if __name__ == "__main__":
    main()
