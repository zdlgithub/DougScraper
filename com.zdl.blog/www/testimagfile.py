#!/usr/bin/python
import urllib
import os

filepath=os.path.abspath('.')
print(filepath)
imgurl='https://ae01.alicdn.com/kf/HTB1sojQadLO8KJjSZPcq6yV0FXah/Outdoor-Suvival-Aluminum-Tactical-Pen-Multi-purpose-Outdoor-Emergency-Break-Glass-Outdoor-Camping-Trip-Kit.jpg'
print('%s'%imgurl.split('/')[-1])
urllib.urlretrieve(imgurl, os.path.join(filepath, '%s'%imgurl.split('/')[-1])) 