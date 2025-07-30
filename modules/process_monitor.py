import psutil, os, time
import logging
from config import CPU_THRESHOLD, MEMORY_THRESHOLD

def run_process_monitor():
    usage = {}
    num_cores = psutil.cpu_count(logical=True)
    for process in psutil.process_iter(['pid', 'ppid', 'name', 'exe',
                                        'cpu_percent', 'memory_info']):

        try:
            # Process Details
            process_name = process.info['name'] or "Unknown"

            # CPU and Memory
            raw_cpu_percent = process.cpu_percent(interval=None)
            cpu_percent = raw_cpu_percent/num_cores
            mem = process.memory_info().rss / (1024 * 1024)

            if process_name not in usage:
                usage[process_name] = {"cpu": 0.0, "mem": 0.0}

            # Combine processes if multiple child processes are running
            usage[process_name]["cpu"] += cpu_percent
            usage[process_name]["mem"] += mem

        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue