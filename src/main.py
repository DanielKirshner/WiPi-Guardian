from common.wifi_scanner import WiFiScanner


def main():
    interface = "wlx00c0ca2a4473"  # Replace with your interface name
    scanner = WiFiScanner(interface)
    scanner.run()

if __name__ == "__main__":
    main()
