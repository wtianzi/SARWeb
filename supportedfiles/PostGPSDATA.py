#!/usr/bin/env python
# coding: utf-8
# Based on restful freamwork
# refer to https://2.python-requests.org//en/latest/user/quickstart/
# 
# In[1]:
import requests

#r = requests.get('http://127.0.0.1:8000/gpsdatas/')

# In[4]:

r = requests.post('http://127.0.0.1:8000/gpsdatas/', data = {'deviceid':'test_2nd', 'taskid':'sar001','gpsdata':'{"gps":["stamp":004,"lat":-80,"log":37]}'})






