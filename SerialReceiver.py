# Helper class to access the serial device
# Copyright 2015 Ethan Smith

import serial
import time

class SerialReceiver(object):

   def __init__(self, port, baudrate):
      self.serial = serial.Serial(port, baudrate)

   def getDataFromReceiver(self):
      data = self.waitForData()
      return self.processData(data)

   def waitForData(self):
      line = ""
      while len(line) < 1:
         time.sleep(1)
         line = self.serial.readline()
      return line


   def processData(self, data):
      divided = data.split('-') # jvwf8-5.36-0

      if len(divided) < 3:
         return None

      return {
         "identifier": divided[0],
         "voltage": divided[1],
         "status": "open" if divided[2] == "0" else "closed"
      }
