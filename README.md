# dualshock4-python
Use either pygame or pyUSB to read inputs from a PS4 dualshock 4 controller

Author: Chi-Feng Pai (cfpai@ieee.org)
Platform: Win10
Python version: 3.6
Main imports: pygame (for joystic, button, and hat inputs) or pyusb+libusb (for gyroscope, accelerator, touch pad inputs)

Quick start:
1. pip install pygame
2. pip install pyusb
3. pip install libusb
4. Modify path to libusb-1.0.dll for backend in the example (e.g. C:\Users\Anaconda3\Lib\site-packages\libusb\_platform\_windows\x86\libusb-1.0.dll)
5. Run the example to get readouts from your dualshock 4 controller
