#system_monitor.py

#Python script to monitor CPU/memory/disk usage

# psutil  is a cross-platform library for 
# retrieving information on running processes and system utilization 

import psutil 
import json
from datetime import datetime

def get_system_metrics(): #function that return the timestamp, CPU/memory/disk usage of your computer
    return {
        "timestamp": str(datetime.now()),
        "cpu_usage": psutil.cpu_percent(interval=1),
        "memory_usage": psutil.virtual_memory().percent,
        "disk_usage": psutil.disk_usage('/').percent
    }

def log_metrics(metrics, filename="system_metrics.log"): # writes metrics into text file
    with open(filename, 'a') as f:
        f.write(json.dumps(metrics) + "\n")

if __name__ == "__main__": #main methof
    metrics = get_system_metrics()
    print(f"Current Metrics: {metrics}")
    log_metrics(metrics)

    # Alert if CPU is greater than 90%
    if metrics["cpu_usage"] > 90:
        print("ALERT: High CPU usage!")