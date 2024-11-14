from dataclasses import dataclass, field

@dataclass
class WiFiNetwork:
    bssid: str
    ssid: str
    beacons_count: int = field(default=0)

    def increment_beacons(self):
        self.beacons_count += 1
