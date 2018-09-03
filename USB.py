# Test your usb connections through pyUSB
# Note that most people will have issues getting anything from devices if the backend hasn't been specifically assigned

import usb.core
import usb.util
import usb.backend.libusb1
import sys

# You have to change the path below to where you placed your libusb-1.0.dll
BACKEND = usb.backend.libusb1.get_backend(find_library=lambda x: "C:\\Users\\Username\\Anaconda3\\Lib\\site-packages\\libusb\\_platform\\_windows\\x64\\libusb-1.0.dll")

dev = usb.core.find(find_all=True)

if dev is None:
    print('Device not found')
else:
    for d in dev:
    	print('Decimal Vendor ID: ' + str(d.idVendor) + ' & ProductID: ' + str(d.idProduct)) # Print all connected USB devices in decimal
    	print('Hexadecimal Vendor ID: ' + hex(d.idVendor) + ' & ProductID: ' + hex(d.idProduct) + '\n') # Print all connected USB devices in hex
