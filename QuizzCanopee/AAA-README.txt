
Configuration PI après démarrage pour Canopée

- mettre a jour la date
 date [-u|--utc|--universal] [MMDDhhmm[[CC]YY][.ss]]

- Lancer l'initialisation de l'environnement Bluetooth
/home/pi/InitBluetoothEnv.sh


=============================================================
- Si le shell InitBluetoothEnv.sh ne permet pas la connexion bluetooth à l'enceinte Bose alors il faut essayer d'executer les commandes ci-dessous

- Lancer le programme python
nohup ./CanopeeSound-mp3.py &

- Redémarrer le service bluetooth
sudo service bluetooth restart

- Connecter l'enceinte Bose
cd /home/pi/Shell
./Bluetooth_Config_Bose.sh | bluetoothctl


- To list pulseaudio connection
pactl list sinks short
0       alsa_output.platform-soc_audio.analog-mono      module-alsa-card.c     s16le 1ch 44100Hz        SUSPENDED
1       bluez_sink.08_EB_ED_71_BF_B2.a2dp_sink  module-bluez5-device.c  s16le 2ch 44100Hz       SUSPENDED



- Si le son n'arrive pas à l'enceinte:
- To establish the link between the require source and sink.
pactl load-module module-loopback source=0 sink=1 rate=44100 adjust_time=0


- Pour envoyer un son mp3 vers l'enceinte:
mpg123 -o pulse filename.mp3
ou
mpg123 filename.mp3

