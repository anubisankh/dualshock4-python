# Use pyUSB to communicate with a dualshock 4 controller

import usb.core
import usb.util
import usb.backend.libusb1
import sys
import os
import time

# DS4 controller ids (might be different on your side)
VENDOR_ID = 0x54c
PRODUCT_ID = 0x9cc

# Don't forget to change the path to libusb-1.0.dll
BACKEND = usb.backend.libusb1.get_backend(find_library=lambda x: "C:\\Users\\Username\\Anaconda3\\Lib\\site-packages\\libusb\\_platform\\_windows\\x64\\libusb-1.0.dll")

dev = usb.core.find(idVendor=VENDOR_ID, idProduct=PRODUCT_ID, backend=BACKEND)
cfg = dev.get_active_configuration()

INTERFACE_DS4 = 3 # HID interface
SETTING_DS4 = 0
interface = cfg[(INTERFACE_DS4, SETTING_DS4)]

ENDPOINT_DS4_OUT = 0 # Input endpoint
endpoint = interface[ENDPOINT_DS4_OUT]

trigger = 0

while trigger != 255: 
	
	os.system('cls')

	# Axes
	print('Readout L stick  X:', format(endpoint.read(0x40)[1],'#04X'), format(endpoint.read(0x40)[1],'08b'), endpoint.read(0x40)[1])
	print('Readout L stick  Y:', format(endpoint.read(0x40)[2],'#04X'), format(endpoint.read(0x40)[2],'08b'), endpoint.read(0x40)[2])
	print('Readout R stick  X:', format(endpoint.read(0x40)[3],'#04X'), format(endpoint.read(0x40)[3],'08b'), endpoint.read(0x40)[3])
	print('Readout R stick  Y:', format(endpoint.read(0x40)[4],'#04X'), format(endpoint.read(0x40)[4],'08b'), endpoint.read(0x40)[4])
	print('Readout L2 trigger:', format(endpoint.read(0x40)[8],'#04X'), format(endpoint.read(0x40)[8],'08b'), endpoint.read(0x40)[8])
	print('Readout R2 trigger:', format(endpoint.read(0x40)[9],'#04X'), format(endpoint.read(0x40)[9],'08b'), endpoint.read(0x40)[9],'\n')

	# Accelerometers (2 bytes to signed integer)
	data = endpoint.read(0x40)
	print('Accelerometer X:', format(256*data[18]+data[19],'016b'), 256*data[18]+data[19]-(65536 if data[18] > 127 else 0))
	print('Accelerometer Y:', format(256*data[16]+data[17],'016b'), 256*data[16]+data[17]-(65536 if data[16] > 127 else 0))
	print('Accelerometer Z:', format(256*data[14]+data[15],'016b'), 256*data[14]+data[15]-(65536 if data[14] > 127 else 0),'\n')

	# Gyroscopes  (2 bytes to signed integer)
	data = endpoint.read(0x40)
	print('Gyroscope X (Roll) :', format(256*data[20]+data[21],'016b'), 256*data[20]+data[21]-(65536 if data[20] > 127 else 0))
	print('Gyroscope Y (Yaw)  :', format(256*data[22]+data[23],'016b'), 256*data[22]+data[23]-(65536 if data[22] > 127 else 0))
	print('Gyroscope Z (Pitch):', format(256*data[24]+data[25],'016b'), 256*data[24]+data[25]-(65536 if data[24] > 127 else 0),'\n')

	# Touch PAD (for more details please refer to the listed references)
	print('Touch PAD:', format(endpoint.read(0x40)[40],'#04X'), format(endpoint.read(0x40)[40],'08b'), endpoint.read(0x40)[40],'\n')

	# Hats
	print("Hats:", endpoint.read(0x40)[5]&15,'\n') #0,1,2,3,4,5,6,7,8

	# Buttons
	print("Square:", endpoint.read(0x40)[5]&16!=0)
	print("Cross:", endpoint.read(0x40)[5]&32!=0)
	print("Circle:", endpoint.read(0x40)[5]&64!=0)
	print("Triangle:", endpoint.read(0x40)[5]&128!=0,'\n')

	# Timestamp
	print('Timestamp:', endpoint.read(0x40)[7]>>2)

	# Battery status
	print('Battery:', endpoint.read(0x40)[30]%16) # 11 means it's Max and charging
	time.sleep(0.1)
	
	trigger = endpoint.read(0x40)[8] # press L2 fully to break
