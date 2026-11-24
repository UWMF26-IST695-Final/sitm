from scapy.layers.l2 import ARP, Ether
from scapy.sendrecv import srp


# ARP opcodes
ARP_WHO_HAS = 1
ARP_IS_AT = 2


def resolve_mac(ip: str, iface: str, timeout: float = 3.0, retries: int = 2) -> str:
    """Resolve an IP to its MAC w/ a real ARP broadcast"""
    request = Ether(dst="ff:ff:ff:ff:ff:ff") / ARP(pdst=ip, op=ARP_WHO_HAS)
    for _ in range(retries + 1):
        answered, _ = srp(request, iface=iface, timeout=timeout, verbose=0)
        for _sent, received in answered:
            return received[ARP].hwsrc
    raise RuntimeError(f"Could not resolve MAC for {ip} on {iface}")
