import time
import threading
from config import SCAN_INTERVAL_SECONDS
import logging

# Import monitoring modules
from modules.process_monitor import main as run_process_monitor
from modules.network_monitor import main as run_network_monitor

def run_modules():
    print(f"🦉 NightWatcher v1.0 is running... Press Ctrl+C to stop.\n")
    try:
        # Run each module synchronously as threads
        proc_monitor_thread = threading.Thread(target=run_process_monitor)
        net_monitor_thread = threading.Thread(target=run_network_monitor)


        # Start each thread
        proc_monitor_thread.start()
        net_monitor_thread.start()

        # Join threads to complete before next cycle
        proc_monitor_thread.join()
        net_monitor_thread.join()

    except Exception as e:
        logging.error(f"Exception while running modules: {e}")


if __name__ == "__main__":
    while True:
        run_modules()
