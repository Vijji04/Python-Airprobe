import pygeoip
import os
import urllib
import requests
my_ip_address=requests.get('https://api.ipify.org').text
print("IP Address : "+my_ip_address)
gip = pygeoip.GeoIP('GeoLiteCity.dat')
res = gip.record_by_addr(my_ip_address)
for key,val in res.items():
	print('%s : %s' % (key,val))
