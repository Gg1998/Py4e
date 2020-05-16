import json
from urllib.request import urlopen

url = input("enter the url")
data = urlopen(url).read()
info = json.loads(data)

sumd = 0
for i in info['comments']:
    sum = sum + int(i['count'])

print(sumd)
