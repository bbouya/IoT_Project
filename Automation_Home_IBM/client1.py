from ast import Import
import time 
import sys
import pprint
import uuid
from uuid import getnode as get_mac


import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(3, GPIO.OUT, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(7, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(11, GPIO.IN)

ls = 'OFF'

try:
    import ibmiotf.application
    import ibmiotf.device
except ImportError:
    # This part is only required to run the sample from within the samples
    # Directory when the module itself is not installed
    # If you have the module installed, just use 'import ibmiotf.application' & "import ibmiotf.device"

    import os 
    import inspect
    cmd_subfolder = os.path.realpath(os.path.abspath(os.path.split(inspect.getfile(inspect.currentframe())[0], "../../src")))
    if cmd_subfolder not in sys.path:
        sys.path.insert(0, cmd_subfolder)
    import ibmiotf.application
    import ibmiotf.device

