# Helper class to access the serial device
# Copyright 2015 Ethan Smith

import serial

class SerialReceiver(object):

   def __init__(self, port, baudrate):
      self.serial = serial.Serial(port, baudrate)
