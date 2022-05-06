# Importation de library 

from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient
from random import randint
import math
import sys
import logging
import time
import json 
import datetime
import argparse
import boto3
import parser   

dynamodb = boto3.resource('dynamodb', region_name = 'YOUR_REGION')  # connection to DynamoDB and access
dynamoTable = dynamodb.Table('YOUR_TABLE_NAME')                     # To the table environmentalstation that will store the data provided
jsonP = ''                                                          # by the two simulated stations

def data_store(client, userdata , msg):                             # The function publishes the recieved data
    payload = str(msg.payload)[2:-1]
    jsonP = json.loads(payload)
    dynamoTable.put_item(Item=jsonP)

def random_values():                                                # The function provides in a simple way random environmental values ....
    temperature = str(randint(-50, 50))
    humidity = str(randint(0, 100))
    wind_direction = str(randint(0, 360))
    wind_intensity = str(randint(0, 100))
    rain_height = str(randint(0, 50))
    datatime = str(datetime.datetime.now())[:19]                     # ... and take notice about the time of the detection, that is important for data storing.
    
    return temperature, humidity, wind_direction, wind_intensity, rain_height, datetime

def awsconnection(useWebsocket = False,
             clientId = '', 
             thingName = 'your_thing_name', 
             host = 'your_endpoint',
             capath = 'your_path/rootCa.pem', 
             certPath = 'your_path/xxxxx-certification.pem.crt', 
             keyPath = 'your_path/xxxxx-private.pem.key'):