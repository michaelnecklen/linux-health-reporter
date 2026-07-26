# Import the timedelta class from the datetime module.
# Use it to represent Serval's elapsed uptime as a readable duration.
from datetime import timedelta

# Import the Path class from the pathlib module.
# Use its read_text() method to read uptime data from /proc/uptime.
from pathlib import Path

# Import the platform module.
# Use its functions to retrieve Serval's kernel and Python versions.
import platform

# Import the shutil module, which provides high-level filesystem utilities.
# Use its disk_usage() function to measure Serval's root filesystem.
import shutil

# Import the socket networking module.
# Use its gethostname() function to retrieve Serval's hostname.
import socket

# Define our own function named get_uptime.
# The empty parameter list means it accepts no arguments; the colon begins its body.
def get_uptime():
    # Create a Path instance for /proc/uptime and call its read_text() method.
    # Assign the returned string to the uptime_text variable.
    uptime_text = Path("/proc/uptime").read_text()

    # Split the text into pieces, select the first piece with [0], and convert
    # that text into a floating-point number assigned to uptime_seconds.
    uptime_seconds = float(uptime_text.split()[0])

    # Convert the seconds to an integer, create a timedelta duration,
    # and return that duration to the code that called get_uptime().
    return timedelta(seconds=int(uptime_seconds))

# Define our function named bytes_to_gib with one parameter named byte_count.
def bytes_to_gib(byte_count):
    # Divide the supplied byte count by the number of bytes in one GiB.
    # Return the resulting GiB value to the code that called this function.
    return byte_count / (1024 ** 3)

# Define our function named get_disk_status with one parameter named percent_used.
# This function assumes the supplied percentage is valid.
def get_disk_status(percent_used):
    # Test the critical threshold first because values at or above 90
    # also satisfy the warning threshold. Return ends this function call.
    if percent_used >= 90:
        return "CRITICAL"
    # If the critical test was false, test whether the value is at least 80.
    # Values from 80 through below 90 return the WARNING string.
    elif percent_used >= 80:
        return "WARNING"
    # If both earlier conditions were false, the value is below 80.
    # Return the OK string to the caller.
    else:
        return "OK"

# Define main(), which coordinates collection, processing, and presentation.
def main():
    # Collect raw system information.
    # Assign to hostname the local machine name returned by socket.gethostname().
    hostname = socket.gethostname()

    # Assign to kernel_version the Linux kernel release returned by platform.release().
    kernel_version = platform.release()

    # Assign to python_version the current interpreter version returned by
    # platform.python_version().
    python_version = platform.python_version()

    # Call our get_uptime() helper with no arguments and assign its returned
    # timedelta instance to uptime.
    uptime = get_uptime()

    # Pass the root filesystem path "/" to shutil.disk_usage().
    # Assign the returned total, used, and free byte counts to disk.
    disk = shutil.disk_usage("/")

    # Convert, calculate, and classify the collected disk information.
    # Pass disk.total in bytes to bytes_to_gib() and assign the returned
    # GiB value to disk_total.
    disk_total = bytes_to_gib(disk.total)

    # Convert the used and free byte counts to GiB and assign the returned
    # values to disk_used and disk_available.
    disk_used = bytes_to_gib(disk.used)
    disk_available = bytes_to_gib(disk.free)

    # Divide used bytes by used plus free bytes to produce a decimal ratio.
    # Multiply that ratio by 100 and assign the resulting percentage to disk_percent.
    disk_percent = disk.used / (disk.used + disk.free) * 100

    # Pass the numeric disk percentage to get_disk_status().
    # Assign the returned OK, WARNING, or CRITICAL string to disk_status.
    disk_status = get_disk_status(disk_percent)

    # Format and display the finished report.
    # Print the fixed report title and a visual underline.
    print("Linux System Health Report")
    print("==========================")

    # Build an f-string by inserting hostname into the fixed label,
    # then pass the finished string to print().
    print(f"Hostname:  {hostname}")

    # Insert the collected kernel, Python, and uptime values into f-strings
    # and display each completed line.
    print(f"Kernel:    {kernel_version}")
    print(f"Python:    {python_version}")
    print(f"Uptime:    {uptime}")

    # Print only a newline, creating a blank line between report sections.
    print()

    # Print the root-filesystem section title and its visual underline.
    print("Root Filesystem")
    print("---------------")

    # Format each GiB value using one digit after the decimal point,
    # insert it into an f-string, and display its fixed GiB unit.
    print(f"Total:        {disk_total:.1f} GiB")
    print(f"Used:         {disk_used:.1f} GiB")
    print(f"Available:    {disk_available:.1f} GiB")

    # Format the numeric percentage with one decimal place and print a fixed % sign.
    print(f"Utilized:     {disk_percent:.1f}%")

    # Insert the status string into an f-string and display the completed line.
    print(f"Status:       {disk_status}")


# Python sets __name__ to "__main__" when this file is run directly.
# If the comparison is true, call main(); when imported, skip this call.
if __name__ == "__main__":
    main()