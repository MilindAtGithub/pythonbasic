#This will give basic info about modules

import sys

v = sys.version_info
print('Python Version {}.{}.{}'.format(*v))
v= sys.platform
print(v)

import os
v1 = os.name
print(v1)
v2 = os.getenv("PATH")
print(v2)
v3 = os.getcwd()
print(v3)

import datetime
now = datetime.datetime.now()
print(now)