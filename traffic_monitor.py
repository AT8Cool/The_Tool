from scapy.all import sniff
import pandas as pd
from collections import defaultdict

traffic_data = []  # Store extracted features
request_count = defaultdict(int)

def process_packet(packet):
    if packet.haslayer("IP"):
        source_ip = packet["IP"].src
        packet_size = len(packet)

        request_count[source_ip] += 1
        traffic_data.append([packet.time, source_ip, packet_size, request_count[source_ip]])

        # Save data periodically
        if len(traffic_data) % 1000 == 0:
            df = pd.DataFrame(traffic_data, columns=["Timestamp", "Source_IP", "Packet_Size", "Request_Count"])
            df.to_csv("network_traffic.csv", index=False)

sniff(prn=process_packet, store=0)