from scapy.all import sniff, IP_PROTOS, TCP_SERVICES, UDP_SERVICES
from datetime import datetime
import socket
import requests
import psutil
import logging


def process_dns_packet(pkt):



def start_dns_monitor():
    print(f"[*] Starting DNS monitoring...")
    sniff(
        filter="udp port 53",
        prn= process_dns_packet,
        store=0
    )
