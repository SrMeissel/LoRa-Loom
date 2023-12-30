import meshtastic
import meshtastic.serial_interface
from pubsub import pub
import time



interface = meshtastic.serial_interface.SerialInterface()

while(True) : 
    time.sleep(1)
    interface.sendData("WHY HELLO THERE")