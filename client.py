import paho.mqtt.client as mqtt
import time
import socket

client_name = 'ml2'
broker_address="localhost" 


print('Starting client', broker_address)


def on_connect(client, userdata, flags, rc):
    if rc==0:
    	client.subscribe("data_frame")
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


while True: #wait in loop
	time.sleep(1)


client.loop_stop()    #Stop loop 
client.disconnect() # disconnect