# -*- coding: utf-8 -*-
"""
Demonstration of relay enables using Numato Lab 4 Channel USB SSR
"""



import PyNumatoRelay
import time
x = 0
while(x<2):
    PyNumatoRelay.relayOn("COM15", "0")
    time.sleep(.25)
    PyNumatoRelay.relayOn("COM15", "1")
    PyNumatoRelay.relayOff("COM15", "0")
    time.sleep(.25)
    PyNumatoRelay.relayOn("COM15", "2")
    PyNumatoRelay.relayOff("COM15", "1")
    time.sleep(.25)
    PyNumatoRelay.relayOn("COM15", "3")
    PyNumatoRelay.relayOff("COM15", "2")
    time.sleep(.25)
    PyNumatoRelay.relayOff("COM15", "3")
    x += 1
x = 0 
while(x<2):
    PyNumatoRelay.relayOn("COM15", "0")
    PyNumatoRelay.relayOn("COM15", "2")
    time.sleep(.25)
    PyNumatoRelay.relayOn("COM15","1" )
    PyNumatoRelay.relayOn("COM15", "3")
    PyNumatoRelay.relayOff("COM15", "0")
    PyNumatoRelay.relayOff("COM15", "2")
    time.sleep(.25)
    PyNumatoRelay.relayOff("COM15", "1")
    PyNumatoRelay.relayOff("COM15", "3")
    x += 1
x = 1
a = .2
while(x<7):
    PyNumatoRelay.relayOn("COM15", "0")
    time.sleep(a)
    PyNumatoRelay.relayOn("COM15", "1")
    time.sleep(a)
    PyNumatoRelay.relayOn("COM15", "2")
    time.sleep(a)
    PyNumatoRelay.relayOn("COM15", "3")
    time.sleep(a)
    x += 1
    PyNumatoRelay.relayOff("COM15", "0")
    time.sleep(a)
    PyNumatoRelay.relayOff("COM15", "1")
    time.sleep(a)
    PyNumatoRelay.relayOff("COM15", "2")
    time.sleep(a)
    PyNumatoRelay.relayOff("COM15", "3")
    time.sleep(a)
    a =.25
    

PyNumatoRelay.relayRead("COM15","0")





