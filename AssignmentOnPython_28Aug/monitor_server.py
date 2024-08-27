## Python program to monitor the health of the CPU

import psutil


def monitor_mac_cpu():
    try:
        cpu_utilization = float(psutil.cpu_percent(interval=1))
        #print(cpu_utilization)
        while True:
            if cpu_utilization>=80:
                print("Monitoring CPU usage...")
                print("Alert! CPU usage exceeds threshold: ", cpu_utilization)
    except KeyboardInterrupt:
        print("\nManual interruption by User!!!")
        
if __name__ == "__main__":
    monitor_mac_cpu()