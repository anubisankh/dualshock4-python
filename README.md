# dualshock4-python
Use either pygame or pyUSB to read inputs from a PS4 dualshock 4 controller through USB connection

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

References:
1. pygame: http://blog.mclemon.io/python-using-a-dualshock-4-with-pygame (Note that the gyroscope and accelerometer won't work if you follow the steps in this reference)
2. pyUSB backend issue: https://c5techblog.wordpress.com/2016/09/05/tutorial-setup-pyusb-under-windows/
3. Detailed mapping of readouts from dualshock 4: http://www.psdevwiki.com/ps4/DS4-USB
4. Other useful resources: https://github.com/seidtgeist/node-ds4 and https://github.com/senceryazici/ps4controller/blob/master/ps4.py
