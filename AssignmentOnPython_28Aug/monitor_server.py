## Python program to monitor the health of the CPU
import psutil

def monitor_mac_cpu():
    try:
        # Calculates the system-wide CPU utilization as a percentage over a 2-second interval.
        cpu_utilization = psutil.cpu_percent(interval=2)  
        print('''
              Do not interrupt.
              Monitoring CPU usage...
              ''')
        while True:
            if cpu_utilization>=80:    # comparing current CPU utilization with threashold value provided as 80.
                print("Alert! CPU usage exceeds threshold: ", cpu_utilization)
    except KeyboardInterrupt:
        print("\nManual interruption by User!!!")
        
if __name__ == "__main__":
    monitor_mac_cpu()
