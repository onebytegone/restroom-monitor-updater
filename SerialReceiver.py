# Helper class to access the serial device
# Copyright 2015 Ethan Smith

import serial

class SerialReceiver(object):

   def __init__(self, port, baudrate):
      self.serial = serial.Serial(port, baudrate)

   def getDataFromReceiver(self):
      data = self.waitForData()
      return self.processData(data)

   def waitForData(self):
      data = self.serial.read()
      time.sleep(1)
      extraData = self.serial.inWaiting()
      data += self.serial.read(extraData)
      return data

   def processData(self, data):
      return data

