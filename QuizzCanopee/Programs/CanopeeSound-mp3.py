#!/usr/bin/env python3
import os
import paho.mqtt.client as mqtt #import the client1
import time

############
def on_message(client, userdata, message):
    print("message received " ,str(message.payload.decode("utf-8")))
    monMes = str(message.payload.decode("utf-8"))
    print("message topic=",message.topic)
    if monMes == "Bon":
        os.system('mpg123 -q -n 100 -o pulse /home/pi/Music/Bruits_Cascade_Oiseaux.mp3')
    else:
        os.system('mpg123 -q -n 100 /home/pi/Music/Bruits_Orage_Pluie.mp3')
    #print("message qos=",message.qos)
    #print("message retain flag=",message.retain)
#############

broker_address="192.168.1.100"
#broker_address="iot.eclipse.org"

print("creating new instance")
client = mqtt.Client("can1")   # create new instance

client.on_message=on_message   # attach function to callback

print("connecting to broker")
client.connect(broker_address) # connect to broker

#client.loop_start()            # start the loop

print("Subscribing to topic","canopee/etat")
client.subscribe("canopee/etat")

time.sleep(4)                  # wait

print("*********** looping  ******************")
try:
    client.loop_forever()
    # deal nicely with ^C 
except KeyboardInterrupt: 
    print("interrupted!")

