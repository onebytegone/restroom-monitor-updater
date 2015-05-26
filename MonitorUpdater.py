#!/usr/bin/python2.7
# Copyright 2015 Ethan Smith

import sys
import os
import ConfigParser
from MonitorAPI import MonitorAPI
from SerialReceiver import SerialReceiver

config = ConfigParser.RawConfigParser()
config.read('app.cfg')

api = MonitorAPI(
   config.get('Server', 'url'),
   config.get('Server', 'secret'),
   config.get('App', 'identifier'),
   config.getint('App', 'expiration')
)

serial = SerialReceiver(
   config.get('Serial', 'port'),
   config.get('Serial', 'baudrate')
)

while 1:
   data = serial.getDataFromReceiver()
   if data != None:
      print "Received: "
      print data
      api.updateStatus(data['status'], data['voltage'], data['identifier'])

