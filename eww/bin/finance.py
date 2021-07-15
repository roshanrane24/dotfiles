#!/bin/env python3

from smartapi import SmartConnect
import os

apikey = os.environ["ANGELAPIKEY"]
clientcode = os.environ["ANGELCLIENTCODE"]
password = os.environ["AGELPASSWORD"]

obj = SmartConnect(api_key=apikey)

data = obj.generateSession(clientCode=clientcode, password=password)
refreshtoken = data['data']['refreshToken']
feedtoken = obj.getfeedToken()
userprofile = obj.getProfile(refreshToken=refreshtoken)
print(userprofile)
