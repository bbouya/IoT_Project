# Importation de library 

from flask import stream_with_context
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



def awsconnection(useWebsocket = False,                                          # the function sets the connection to AWS
    clientId = "",                                                               # client id
    thingName = "YOUR_THING_NAME",                                               # thing name (on AWS)
    host = "YOUR_ENDPOINT",                                                      # your AWS endpoint
    caPath = "YOUR_PATH/rootCa.pem",                                             # rootCA certificate (folder's path)
    certPath = "YOUR_PATH/XXXXXXXXXX-certificate.pem.crt",                       # client certificate (folder's path)
    keyPath = "YOUR_PATH/XXXXXXXXXX-private.pem.key"                             # private key (folder's path)
    ):

    port = 8883 if not useWebsocket else 443
    useWebsocket = useWebsocket
    clientId = clientId
    host = host
    port = port
    rootCaPath = caPath
    privateKeyPath = keyPath
    certificatePath = certPath

    # Logger settings
    # more information at https://docs.python.org/3/library/logging.html
    logger = logging.getLogger("AWSIoTPythonSDK.core")
    logger.setLevel(logging.NOTSET)                                                      # NOTSET causes all messages to be processed when the logger is the root logger
    streamHandler = logging.StreamHandler()                                              # sends logging output to streams
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    streamHandler.setFormatter(formatter)
    logger.addHandler(streamHandler)

    # AWSIoTMQTTClient initialization
    myClient = None
    if useWebsocket:
        myClient = AWSIoTMQTTClient(clientId, useWebsocket=True)
        myClient.configureEndpoint(host, port)
        myClient.configureCredentials(rootCaPath)
    else:
        myClient = AWSIoTMQTTClient(clientId)
        myClient.configureEndpoint(host, port)
        myClient.configureCredentials(rootCaPath, privateKeyPath, certificatePath)

    # AWSIoTMQTTClient connection configuration
    myClient.configureAutoReconnectBackoffTime(1, 32, 20)
    myClient.configureOfflinePublishQueueing(-1)      # param: if set to 0, the queue is disabled. If set to -1, the queue size is set to be infinite.
    myClient.configureDrainingFrequency(2)            # Draining: 2 Hz
    myClient.configureConnectDisconnectTimeout(10)    # 10 sec
    myClient.configureMQTTOperationTimeout(5)         # 5 sec

    return myClient

# Arguments passing : in this case the only argument that we need is the clientID, that is supposed to be station1 or station2
parser = argparse.ArguementParser()
parser.add_arguement('--clientis', type = str)
args = parser.parse_args()
clientId = args.clientid
topic = 'YOUR TOPICS'

myClient = awsconnection(clientId=clientId)