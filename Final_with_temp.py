import pygeoip
import os
import urllib
import requests
from pprint import pprint
my_ip_address=requests.get('https://api.ipify.org').text
print("IP Address : "+my_ip_address)
gip = pygeoip.GeoIP('GeoLiteCity.dat')
res = gip.record_by_addr(my_ip_address)
for key,val in res.items():
	if(key=='city'):
		city=val
	print('%s : %s' % (key,val))

url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=1b47a5e4ecd7a05369c6bb2054431293&units=metric'.format(city)

res = requests.get(url)

data = res.json()
temp = data['main']['temp']

print('Temperature : {} degree celcius'.format(temp))


