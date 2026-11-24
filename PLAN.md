# plan

- `arpspoof.py` contains `Spoofer`
  - Initialize with: target IP, gateway IP, interface name, response interval, # of packets sent when restoring unpoisoned cache
  - `start()` and `stop()` to start and stop spoofing
  - Constructs both "who has" and "is at" ARP packet frames using scapy library, answering as "who has" to the server and gateway to initiate MITM
- `packetsniff.py` contains `Sniffer`
  - Initialize with an interface name
  - Only works if ARP spoofing is running
  - `start()` starts and keeps running sniffer output until interruped by Ctrl-C

- `utils.py` any other helper functions made along the way, in addition to:
  - `get_host_mac` - get MAC of the current host
  - `get_gateway_address` - get gatway address

- `probe.py` allows listing of hosts
  - Prober initializes with interface name
  - `show` returns a list of hosts, each host represented as a set key-value pairs containing IP, hostname, mac address

- `mitm.py` abstracts spoofing and packet sniffing into one `MITM`
  - Initialize with: target IP, interface name, whether or not to use full duplex (?), and any other packet sniffing options
  - Contains `attack()` which starts ARP spoofing, then begins printing network traffic using the `Sniffer`

- `cli.py` processes command line arguemnts:
  - at the very least, requires `-i <interface>`
  - `--list-hosts` prints a table/list of hosts on the network
  - if `--list-hosts` not used, require a target IP address after interface
  - `--ful-duplex` ?
  - print a reasonable help message with `--help`
