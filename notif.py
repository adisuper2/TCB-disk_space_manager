import psutil
from win10toast import ToastNotifier
import time

threshold = 80
def notify_disk_usage():
    toaster = ToastNotifier()
    
    while True:
        disk_usage = psutil.disk_usage('/')
        used = disk_usage.percent
        if used > threshold:
            message = f"Disk usage is at {used}%.\nPlease free up some disk space."
            toaster.show_toast("Disk Usage Alert", message, duration=10)

        time.sleep(8*60*60)

if __name__ == "__main__":
    notify_disk_usage()
