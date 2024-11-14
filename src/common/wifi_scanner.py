
from scapy.all import *
from threading import Thread
from time import sleep
import os

from common.wifi_network import WiFiNetwork


RESULT_REFRESH_INTERVAL = 2  # Time between result updates in seconds


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
        print("BSSID\t\t\tBeacons\t\tESSID")
        print("-" * 50)
        for network in self.__networks.values():
            print(f"{network.bssid}  {network.beacons:7d}    {network.ssid}")

    def __change_channel(self):
        MAX_2G_CHANNEL = 14  # Maximum number of channels in 2.4 GHz band
        CHANNEL_SWITCH_INTERVAL = 0.5  # Time between channel switches in seconds

        channel = 1
        while True:
            os.system(f"iwconfig {self.__interface} channel {channel}")
            channel = channel % MAX_2G_CHANNEL + 1
            sleep(CHANNEL_SWITCH_INTERVAL)

    def run(self, scanning_duration_in_seconds=60):
        channel_changer = Thread(target=self.__change_channel)
        channel_changer.daemon = True
        channel_changer.start()

        print(f"Scanning on {self.__interface} for {scanning_duration_in_seconds} seconds...")
        
        start_time = time.time()
        while time.time() - start_time < scanning_duration_in_seconds:
            sniff(iface=self.__interface, prn=self.__callback, timeout=RESULT_REFRESH_INTERVAL)
            self.__print_results()

