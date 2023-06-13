import json
import requests

url = 'https://api.bluelytics.com.ar/v2/latest'

r = requests.get(url)
data=json.loads(r.text)
x_rate = data['oficial']['value_sell']
print(data)
print(x_rate)
