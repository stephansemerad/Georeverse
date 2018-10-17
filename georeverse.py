#!/usr/bin/python
## -*- coding: utf-8 -*-
import os, re,random, string, sys,  os.path, time
dir_path = os.path.dirname(os.path.realpath(__file__))
parent = os.path.abspath(os.path.join(dir_path, os.pardir))
sys.path.append(parent)

from datetime import datetime
import xmltodict
from urllib.request import urlopen
from decimal import Decimal

from bs4 import BeautifulSoup
import json
import ast


API_KEY = 'XXXXXXX'
# Lat & Long from Madrid
lat     = '40.4168'
lng     = '3.7038'

url = "https://maps.googleapis.com/maps/api/geocode/json?key="+str(API_KEY)+"&amp;&latlng="+lat+","+lng+"&sensor=false"
html = urlopen(url)
soup = BeautifulSoup(html, "html.parser") #Get the HTML

_json = json.dumps(str(soup))
dictionary = json.loads(_json)
dictionary = ast.literal_eval(dictionary)
dictionary = dictionary['results'][0]['address_components']
