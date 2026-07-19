from datetime import timedelta
from pathlib import Path
import socket
import platform


def get_uptime():
    uptime_text = Path("/proc/uptime").read_text()
    uptime_seconds = float(uptime_text.split()[0])
    return timedelta(seconds=int(uptime_seconds))

hostname = socket.gethostname()
python_version = platform.python_version()
uptime = get_uptime()

print("Linux System Health Report")
print("==========================")
print(f"Hostname:  {hostname}")
print(f"Python:    {python_version}")
print(f"Uptime:    {uptime}")
