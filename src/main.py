from dataclasses import dataclass, field
from scapy.all import *
from threading import Thread
import time
import os


MAX_2G_CHANNEL = 14  # Maximum number of channels in 2.4 GHz band
CHANNEL_SWITCH_INTERVAL = 0.5  # Time between channel switches in seconds
RESULT_REFRESH_INTERVAL = 2  # Time between result updates in seconds
SCAN_DURATION = 60  # Total duration of scanning in seconds

@dataclass
class WiFiNetwork:
    bssid: str
    ssid: str
    beacons: int = field(default=0)

    def increment_beacons(self):
        self.beacons += 1

class WiFiScanner:
    def __init__(self, interface):
        self.__interface = interface
        self.__networks = {}

    def __callback(self, packet):
        if packet.haslayer(Dot11Beacon):
            bssid = packet[Dot11].addr2
            ssid = packet[Dot11Elt].info.decode(errors='ignore')
            
            if bssid not in self.__networks:
                self.__networks[bssid] = WiFiNetwork(bssid, ssid)
            
            self.__networks[bssid].increment_beacons()

    def __print_results(self):
        os.system('clear')
        print("BSSID              Beacons    ESSID")
        print("-" * 50)
        for network in self.__networks.values():
            print(f"{network.bssid}  {network.beacons:7d}    {network.ssid}")

    def __change_channel(self):
        channel = 1
        while True:
            os.system(f"iwconfig {self.__interface} channel {channel}")
            channel = channel % MAX_2G_CHANNEL + 1
            time.sleep(CHANNEL_SWITCH_INTERVAL)

    def run(self):
        channel_changer = Thread(target=self.__change_channel)
        channel_changer.daemon = True
        channel_changer.start()

        print(f"Scanning on {self.__interface} for {SCAN_DURATION} seconds...")
        
        start_time = time.time()
        while time.time() - start_time < SCAN_DURATION:
            sniff(iface=self.__interface, prn=self.__callback, timeout=RESULT_REFRESH_INTERVAL)
            self.__print_results()

        print("Scan completed.")

def main():
    interface = "wlx00c0ca2a4473"  # Replace with your interface name
    scanner = WiFiScanner(interface)
    scanner.run()

if __name__ == "__main__":
    main()