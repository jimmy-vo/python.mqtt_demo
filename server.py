import paho.mqtt.client as mqtt
import time
import socket


client_name = 'ml1'
topic = 'data_frame'
broker_address="localhost" 


print('Starting client', broker_address)


def on_connect(client, userdata, flags, rc):
    if rc==0:
        pass
    else:
        print("Bad connection Returned code=",rc)


def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))


client = mqtt.Client(client_name)
client.on_connect = on_connect
client.on_message = on_message
client.connect(broker_address)
client.loop_start()  #Start loop 
time.sleep(4) # Wait for connection setup to complete

for i in range(3000):
	client.publish(topic,str(i))
	print('published:', i)
	time.sleep(1)


client.loop_stop()    #Stop loop 
client.disconnect() # disconnect