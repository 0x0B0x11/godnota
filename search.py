#! /bin/python

import requests, re

proxies = {
    "http": "http://127.0.0.1:4444",
    "https": "http://127.0.0.1:4444",
}

r = requests.get('http://shx5vqsw7usdaunyzr2qmes2fq37oumybpudrd4jjj4e4vk4uusa.b32.i2p/', proxies=proxies).text


print(r)
s = re.finditer(r'\w{52}\.b32\.i2p', r)
n = next(s)
print(n.group())
