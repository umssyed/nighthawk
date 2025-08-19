from scapy.all import sniff, IP_PROTOS, TCP_SERVICES, UDP_SERVICES
from datetime import datetime
import socket
import requests
import psutil, os, time
import logging
from config import CPU_THRESHOLD, MEMORY_THRESHOLD, SCAN_INTERVAL_SECONDS

# Port Scanning for malicious activity
# Port 20 (UDP) - File Transfer Protocol for data transfer
# Port 22 (TCP) - SSH protocol for secure logins, FTP and port forwarding
# Port 23 (TCP) - Telenet protocol for unencrypted text commutations
# Port 53 (UDP) - DNS translates names of all computer on internet to IP address
# Port 80 (TCP) - Internet HTTP


def process_dns_packet(pkt):
    pass


def start_monitor():
    print(f"[*] Starting DNS monitoring...")
    sniff(
        filter="udp port 53",
        prn= process_dns_packet,
        store=0
    )


def main():
    print(f"== Network Monitor Thread ==")
    while True:
        start_monitor()
        time.sleep(SCAN_INTERVAL_SECONDS)