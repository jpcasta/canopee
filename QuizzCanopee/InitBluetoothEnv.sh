#!/bin/bash

# Commands to connect bluetooth speaker for Canopee program
# Restart bluetooth service
sudo service bluetooth restart
sleep 2

# Start python process to play music on bluetooth speaker
nohup /home/pi/Programs/CanopeeSound-mp3.py &

# Connect Bose Bluetooth speaker
/home/pi/Shell/Bluetooth_Config_Bose.sh | bluetoothctl


