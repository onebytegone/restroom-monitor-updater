#!/usr/bin/python2.7
# Copyright 2015 Ethan Smith

import sys
import os
import ConfigParser
from MonitorAPI import MonitorAPI

config = ConfigParser.RawConfigParser()
config.read('app.cfg')

api = MonitorAPI(
   config.get('Server', 'url'),
   config.get('Server', 'secret'),
   config.get('App', 'identifier'),
   config.getint('App', 'expiration')
)
print api.updateStatus('open')
