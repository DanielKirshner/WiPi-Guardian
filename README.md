# WiPi Guardian

WiPi Guardian is a Raspberry Pi-based security tool designed to enhance the security of your Wi-Fi network.
It actively monitors for suspicious probe requests on your network and notifies you of any detected MAC addresses that may indicate potential threats.

## What is a Probe Request?

In Wi-Fi networks, a probe request is a type of management frame that is broadcasted by wireless devices (like smartphones, laptops, etc.) to discover nearby Wi-Fi networks. When a device is not connected to any network, it sends out probe requests to find available access points. These requests may contain the device's MAC address and can sometimes include information about previously connected networks.
Probe requests are a valuable tool for legitimate network operations but can also be exploited by malicious actors to gather information about a network or to impersonate devices.

## Features

- **Real-Time Probe Request Monitoring**: Continuously monitors your Wi-Fi network for probe requests to identify potential threats.
- **MAC Address Notification**: Alerts you when a suspicious MAC address is detected, enabling you to take immediate action.
- **Lightweight and Efficient**: Runs on a Raspberry Pi, making it a cost-effective and portable solution for network security.
- **Customizable Alerts**: Set up notifications to suit your security needs, whether via email, SMS, or other messaging services.

## Prerequisites

- Raspberry Pi (any model with Wi-Fi capability)
- External Wi-Fi adapter (optional, for extended range)
- Access to the internet for setting up dependencies #TODO: make a full deb package install file for offline usage

## Configuration

- **Interface**: The interface to scan with (internal rpi wi-fi or external adapter)
- **Notification Settings**: You can customize how you receive alerts (e.g., Telegram, email, SMS).
- **Whitelist**: Add trusted MAC addresses to a whitelist to avoid false positives.

## Contributing

* Contributions are welcome!
* Please fork the repository and submit a pull request for review.
* Feel free to adjust any sections to better fit your specific implementation or preferences!

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
