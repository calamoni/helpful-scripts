#!/usr/bin/python

import subprocess

addresses = [redacted]

mac = "redacted"

print("######################################################################")
print("Hi, I am your friendly neighborhood Spooderman. Let me add those ARP entries for you, lazy fuck.")
print("######################################################################")


for address in addresses:
    print("Checking if ARP entry exists......")
    if "no entry" not in subprocess.run(["arp", "-n", address], capture_output=True, text=True).stdout:
        print(f"ARP entry exists for {address}")
    else:
        print(f"Adding ARP entry for {address}")
        subprocess.run(["sudo", "arp", "-s", address, mac])
