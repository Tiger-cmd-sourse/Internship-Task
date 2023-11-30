# Install necessary libraries
pip install scapy pandas matplotlib seaborn scikit-learn libpcap

import scapy.all as scapy
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.ensemble import IsolationForest

def sniff_packets(interface, filter, output_file):
    print(f"Sniffing packets on {interface}...")

    # Use sniff function to capture packets
    packets = scapy.sniff(iface=interface, store=True, prn=lambda x: process_packet(x, output_file), filter=filter)

def process_packet(packet, output_file):
    # Extract relevant information from the packet
    packet_info = {
        "Timestamp": packet.time,
        "Source": packet[scapy.IP].src,
        "Destination": packet[scapy.IP].dst,
        "Protocol": packet[scapy.IP].proto,
        "Length": len(packet),
    }

    # Check if the packet is TCP
    if scapy.TCP in packet:
        packet_info["TCP_Flags"] = packet.sprintf("%TCP.flags%")
    else:
        packet_info["TCP_Flags"] = None

    # Display packet details
    print("\nPacket Details:")
    print("Timestamp:", packet_info["Timestamp"])
    print("Source IP:", packet_info["Source"])
    print("Destination IP:", packet_info["Destination"])
    print("Protocol:", packet_info["Protocol"])
    print("Length:", packet_info["Length"])
    print("TCP Flags:", packet_info["TCP_Flags"])

    # Append the packet information to the output file
    with open(output_file, 'a') as file:
        pd.DataFrame([packet_info]).to_csv(file, header=not file.tell(), index=False)

# Usage
# sniff_packets("eth0", "tcp or udp", "packet_details.csv")

def analyze_packets(output_file):
    # Read the captured packet details from the CSV file
    df = pd.read_csv(output_file)

    # Basic analysis, e.g., count of packets per protocol
    protocol_counts = df['Protocol'].value_counts()
    print("Protocol Counts:")
    print(protocol_counts)

    # Visualization (using Matplotlib and Seaborn)
    plt.figure(figsize=(10, 6))
    sns.countplot(data=df, x='Protocol')
    plt.title('Protocol Distribution')
    plt.show()

    # Statistical analysis of packet length
    mean_length = df['Length'].mean()
    std_length = df['Length'].std()

    # Identify outliers using z-score
    df['Length_ZScore'] = (df['Length'] - mean_length) / std_length
    outliers = df[df['Length_ZScore'].abs() > 3]  # Adjust threshold as needed

    print("Outliers based on Length:")
    print(outliers)

def detect_anomalies(output_file):
    # Read the captured packet details from the CSV file
    df = pd.read_csv(output_file)

    # Use Isolation Forest for anomaly detection
    model = IsolationForest(contamination=0.05)  # Adjust contamination based on your dataset
    df['Anomaly'] = model.fit_predict(df[['Protocol', 'Length']])

    # Display anomalies
    anomalies = df[df['Anomaly'] == -1]
    print("Anomalies:")
    print(anomalies)

# Usage
sniff_packets("eth0", "tcp or udp", "packet_details.csv")
analyze_packets("packet_details.csv")
detect_anomalies("packet_details.csv")

