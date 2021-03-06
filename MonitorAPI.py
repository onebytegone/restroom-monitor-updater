# Helper class to access the restroom monitor api
# Copyright 2015 Ethan Smith

import urllib
import urllib2
import json
import jwt

class MonitorAPI(object):

   def __init__(self, url, secret, identifier, expiration):
      self.server = url.rstrip('/')
      self.secret = secret
      self.identifier = identifier
      self.expiration = expiration

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

   def status(self):
      response = self.sendMessage('GET', '/v1/status', '')
      return response

   def updateStatus(self, status, voltage = "", remoteIdent = ""):
      response = self.ping()
      serverTime = response['time']
      jwt = self.createStatusJWT(status, voltage, remoteIdent, serverTime)
      response = self.sendMessage('POST', '/v1/update', jwt)
      return response

   def createStatusJWT(self, status, voltage, remoteIdent, currentTime):
      return self.createJWT({
         'status': status,
         'voltage': voltage,
         'remoteIdent': remoteIdent,
         'time': currentTime,
         'identifier': self.identifier,
         'exp': currentTime+self.expiration
      })

   def createJWT(self, data):
      return jwt.encode(data, self.secret, algorithm='HS512')
