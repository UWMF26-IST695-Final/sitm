from . import arpspoof
from . import packetsniff
from . import utils


class MITM:
    def __init__(self, target: str, interface: str, full_duplex: bool = True):
        self.target = target
        self.interface = interface
        self.full_duplex = full_duplex

    def attack(self):
        pass
