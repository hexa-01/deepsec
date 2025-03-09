import joblib
import numpy as np
from scapy.all import sniff, IP, TCP, UDP, ICMP
from rich.console import Console

console = Console()

attack_signatures = {
    "SYN Scan": lambda pkt: pkt.haslayer(TCP) and pkt[TCP].flags == "S",
    "DNS Poisoning": lambda pkt: pkt.haslayer(UDP) and pkt[UDP].sport == 53 and "malicious.com" in str(pkt),
    "ICMP Flood": lambda pkt: pkt.haslayer(ICMP) and pkt[ICMP].type == 8
}

def packet_callback(packet):
    for attack, check in attack_signatures.items():
        if check(packet):
            src = packet[IP].src if packet.haslayer(IP) else "Unknown"
            dst = packet[IP].dst if packet.haslayer(IP) else "Unknown"
            console.print(f"[bold red]🚨 كشف هجوم {attack}: {src} -> {dst}[/bold red]")

def scan_protocols(interface):
    console.print(f"[bold cyan]🌐 جاري فحص البروتوكولات على الواجهة: {interface}[/bold cyan]")
    sniff(iface=interface, prn=packet_callback, store=False)

model = joblib.load("network_anomaly_model.pkl")

def extract_features(packet):
    features = []
    if packet.haslayer(IP):
        features.append(len(packet))  
        features.append(packet[IP].ttl)  
    else:
        features.extend([0, 0])
    return np.array(features).reshape(1, -1)

def ml_packet_analysis(packet):
    if packet.haslayer(IP):
        features = extract_features(packet)
        prediction = model.predict(features)
        if prediction == 1:
            console.print(f"[bold red]🚨 كشف هجوم مشبوه من {packet[IP].src}[/bold red]")

def scan_with_ml(interface):
    console.print(f"[bold cyan]🧠 تحليل الشبكة باستخدام الذكاء الاصطناعي على {interface}[/bold cyan]")
    sniff(iface=interface, prn=ml_packet_analysis, store=False)
