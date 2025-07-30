import time
import threading
from config import SCAN_INTERVAL_SECONDS

# Import monitoring modules
from modules.process_monitor import run_process_monitor

if __name__ == "__main__":
    while True:
        run_process_monitor()
        time.sleep(SCAN_INTERVAL_SECONDS)
