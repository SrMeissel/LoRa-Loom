import meshtastic
import meshtastic.serial_interface
from pubsub import pub

def onReceive(packet, interface): # called when a packet arrives
    print(f"Received: {packet} \n")

def onConnection(interface, topic=pub.AUTO_TOPIC): # called when we (re)connect to the radio
    # defaults to broadcast, specify a destination ID if you wish
    print("Device connected \n")
    interface.sendText("hello mesh")


# function passed in subscribed is called everytime a new message is published to topic. 
pub.subscribe(onReceive, "meshtastic.receive.decoded.payload")
pub.subscribe(onConnection, "meshtastic.connection.established")
# By default will try to find a meshtastic device, otherwise provide a device path like /dev/ttyUSB0
interface = meshtastic.serial_interface.SerialInterface()

while(True) : 
    True