from json_parser import *

from typing import List
import logging
import netifaces
import subprocess

class InterfaceNotFoundError(Exception):
    pass

class InvalidInterface(Exception):
    pass

class NotWirelessInterface(Exception):
    pass

class Interface():
    def __init__(self): 
        self.name = get_value_from_json(get_json_as_dict(), JsonKeys.interface.value)
        self.interface_exists = self._interface_exists()
        self.up = self._check_if_interface_is_up()
        self.mode = self._get_interface_mode()
        self._validate()


    def _interface_exists(self) -> bool:
        """
        Check if the interface connected and exists.
        Raises:
            InterfaceNotFoundError: interface not found in the list of interfaces

        Returns:
            bool: is exits?
        """
        interface_exists = self.name in netifaces.interfaces()
        if interface_exists == False:
            logging.error(f"Interface {self.name} does not exists.")
            raise InterfaceNotFoundError()
        return interface_exists

    
    def _get_cmd_output(self, command_to_execute: List[str]) -> str:
        """
        Wrapper function for subprocess handling.
        Args:
            command_to_execute (List[str]): command to run as a list (subprocess format)

        Raises:
            NotWirelessInterface: the interface does not support wifi

        Returns:
            str: output of the command
        """
        output = ''
        try:
            output = str(subprocess.check_output(command_to_execute))
        except subprocess.CalledProcessError as e:
            logging.error(f"{e}\n{self.name} is not a wireless interface.")
            raise NotWirelessInterface()
        return output


    def _check_if_interface_is_up(self) -> bool:
        """
        Check if the interface is on 'UP' mode in order to work with it.
        Returns:
            bool: is interface up?
        """
        command = ["ip", "link", "show", "up"]
        return self.name in self._get_cmd_output(command)
    

    def _get_interface_mode(self) -> str:
        """
        Get the interface current scan mode
        Returns:
            str: Mode (managed / monitor)
        """
        command = ["iwconfig", self.name]
        if "Mode:Monitor" in self._get_cmd_output(command):
            return "monitor"
        return "managed"


    def _validate(self):
        """
        Validate that the interface exists, up and in managed mode.
        Raises:
            InvalidInterface: the interface is not valid to work with
        """
        if self.interface_exists and self.up and self.mode == "managed":
            return
        logging.error(f"Invalid interface {self}\nInterface details:\n")
        raise InvalidInterface()
    

    def recheck(self):
        """
        Rechecking for interface changes while scanning, same like the c'tor but without name initialization.
        """
        self.interface_exists = self._interface_exists()
        self.up = self._check_if_interface_is_up()
        self.mode = self._get_interface_mode()
        self._validate()
    
    
    def enter_monitor_mode(self):
        """
        TODO: Wrap those base commands with safe subprocess call:
        
            systemctl mask wpa_supplicant
            systemctl stop wpa_supplicant
            ip link set dev self.name down
            iwconfig self.name mode monitor
            ip link set dev self.name up
        """
        pass
    
    
    def enter_managed_mode(self):
        """
        TODO: Wrap those base commands with safe subprocess call:
        
            systemctl unmask wpa_supplicant
            ip link set dev self.name down
            iwconfig self.name mode managed
            ip link set dev self.name up
            systemctl restart wpa_supplicant
        """
        pass
        

    def __str__(self) -> str:
        """
        Presents the interface values
        Returns:
            str: Interface as str
        """
        return f"Interface name = {self.name}\nInterface up = {self.up}\nInterface mode = {self.mode}"
