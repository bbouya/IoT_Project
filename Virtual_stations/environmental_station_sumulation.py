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

def data_store(client, userdata , msg):
    payload = str(msg.payload)[2:-1]
    jsonP = json.loads(payload)
    dynamodb
