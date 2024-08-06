# -*- coding: utf-8 -*-
"""
numatoRelay

Python functions to interface with NumatoRelay
Define port as string "COM" ex: port = "COM15"
Define relay as string with 0 indexing ex: relay = "0"

"""
import serial
import codecs


def relayOn(port, relay):
    """
    Turns target relay ON.

    Parameters
    ----------
    port : STRING
        Define Com port of numatoRelay ex: "COM15".
    relay : STRING
        Define target relay ex: "0".

    Returns
    -------
    None.

    """
    portName = port
    relayNum = relay
    relayCmdOn = "on"
    serPort = serial.Serial(portName, 19200, timeout=1)
    toWriteOn = "relay "+ str(relayCmdOn) +" "+ str(relayNum) + "\n\r"
    serPort.write(bytes(toWriteOn, encoding='utf8'))
    serPort.close()

def relayOff(port, relay):
    """
    Turns target relay OFF.

    Parameters
    ----------
    port : STRING
        Define Com port of numatoRelay ex: "COM15".
    relay : STRING
        Define target relay ex: "0".

    Returns
    -------
    None.

    """
    portName = port
    relayNum = relay
    relayCmdOff = "off"
    serPort = serial.Serial(portName, 19200, timeout=1)
    toWriteOff = "relay "+ str(relayCmdOff) +" "+ str(relayNum) + "\n\r"
    serPort.write(bytes(toWriteOff, encoding='utf8'))
    serPort.close()

def relayRead(port, relay):
    """
    Reads target relay. 

    Parameters
    ----------
    port : STRING
        Define Com port of numatoRelay ex: "COM15".
    relay : STRING
        Define target relay ex: "0".

    Returns
    -------
    1 if relay is on.
    0 if relay is off.

    """
    portName = port
    relayNum = relay
    serPort = serial.Serial(portName, 19200, timeout=1)
    toWrite = "relay read "+ str(relayNum) + "\n\r"
    serPort.write(codecs.encode(toWrite, encoding = 'utf8'))
    response = serPort.read(25)
    if(response.find(bytes("on", encoding = 'utf8')) > 0):
        print ("Relay " + str(relayNum) +" is ON")
        return(1)

    elif(response.find(bytes("off", encoding = 'utf8')) > 0):
        print ("Relay " + str(relayNum) +" is OFF")
        return(0)
    serPort.close()
