import asyncio
from msilib.schema import PublishComponent

from cv2 import connectedComponents

from hbmqtt.client import MQTTClient
from hbmqtt.mqtt.constants import QOS_0, QOS_1,QOS_2


async def publish_test():
    try:
        C = MQTTClient()
        ret = await C.connect('mqtt://192.168.0.4:1883/')
        message = await C.publish('server', 'MESSAGE-QOS_0'.encode(), qos = QOS_0)
        message = await C.publish('server','MESSAGE-QOS_1'.encode(), qos = QOS_1)
        message = await C.publish('geteway', 'MESSAGE-QOS_2'.encode(), qos = QOS_2)
        print('Message published')

        await C.disconnect()
    except ConnectException  as ce:
        print('connection Failed: %s' % ce)
        asyncio.get_event_loop().stop()

if __name__  == '__main__':
    asyncio.get_event_loop().run_until_complete(publish_test())

