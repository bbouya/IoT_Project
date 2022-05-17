# Import de library

from ast import While
from pickle import REDUCE, TRUE
import time 
import sys 
import os
from tkinter import W
import requests 
import json 

import iothub_client
 


from iothub_client import IoTHubModuleClient, IoTHubClientError, IoTHubTransportProvider
from iothub_client import IoTHubMessage, IoTHubMessageDispositionResult, IoTHubError

import RPI.GPIO as GPIO 
GPIO.setmode(GPIO.BMC)

white = 5 
yellow = 6 
blue = 13 
green = 19 
red = 26

GPIO.setup(white, GPIO.OUT)
GPIO.setup(yellow, GPIO.OUT)
GPIO.setup(blue, GPIO.OUT)
GPIO.setup(green, GPIO.OUT)
GPIO.setup(red, GPIO.OUT)

def show_result_led(classify):
    if classify == 'A':
        light = yellow
    elif classify == "B":
        light = blue
    elif classify == 'C':
        light = green
    elif classify == 'D':
        light = red
    else : 
        light = white

    switch(light)

def switch(light):
    GPIO.output(red, red == light)
    GPIO.output(blue, blue == light)
    GPIO.output(green, green == light)
    GPIO.output(yellow, yellow == light)
    GPIO.output(white, white == light)


# All lights on 
def all_lights():
    GPIO.output(red, True)
    GPIO.output(blue, True)
    GPIO.output(green, True)
    GPIO.output(yellow, True)
    GPIO.output(white, True)

# all lights off
def no_lights():
    GPIO.output(red, False)
    GPIO.output(blue, False)
    GPIO.output(green, False)
    GPIO.output(yellow, False)
    GPIO.output(white, False)

# Status indicator: white lighto
def processing():
    switch(white)

