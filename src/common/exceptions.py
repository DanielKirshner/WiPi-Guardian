class InterfaceExceptions:
    class InterfaceNotFoundError(Exception):
        def __init__(self, message: str = "Interface not found in the list of interfaces"):
            self.message = message
            super().__init__(self.message)

    class InvalidInterface(Exception):
        def __init__(self, message: str = "Invalid interface name"):
            self.message = message
            super().__init__(self.message)

    class NotWirelessInterface(Exception):
        def __init__(self, message: str = "Not wireless interface"):
            self.message = message
            super().__init__(self.message)