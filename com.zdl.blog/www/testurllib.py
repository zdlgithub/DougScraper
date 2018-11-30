# -*- coding: utf-8 -*- 
from urllib import request

req = request.Request('https://www.aliexpress.com/store/product/Outdoor-Suvival-Aluminum-Tactical-Pen-Multi-purpose-Outdoor-Emergency-Break-Glass-Outdoor-Camping-Trip-Kit/1708277_32841619817.html?spm=2114.12010612.8148356.1.514d4cdcW7STCF')
# req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
with request.urlopen(req) as f:
    print('Status:', f.status, f.reason)
    for k, v in f.getheaders():
        print('%s: %s' % (k, v))
    print('Data:', f.read().decode('utf-8'))