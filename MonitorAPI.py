# Helper class to access the restroom monitor api
# Copyright 2015 Ethan Smith

import urllib
import urllib2
import json

class MonitorAPI(object):

   def __init__(self, url, secret, identifier):
      self.server = url.rstrip('/')
      self.secret = secret
      self.identifier = identifier

   def sendMessage(self, method, command, jwt):
      url = self.server+command
      print "Request: " + method + " " + url
      req = urllib2.Request(url)
      req.add_header('identifier', self.identifier)
      req.add_header('jwt', jwt)
      req.get_method = lambda: method
      response = urllib2.urlopen(req)
      data = response.read()
      return json.loads(data)

   def ping(self):
      response = self.sendMessage('GET', '/v1/ping', '')
      return response
