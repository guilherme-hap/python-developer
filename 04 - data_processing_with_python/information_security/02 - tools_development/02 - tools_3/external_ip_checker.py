"""
    Programa que utiliza das bibliotecas 'json' e 'urllib' para implementar um verificador
    de IP externo.
"""
import json
from urllib.request import urlopen

url = 'https://ipinfo.io/json'

response = urlopen(url)

data = json.load(response)

ip = data['ip']
org = data['org']
city = data['city']
country = data['country']
region = data['region']

print("External IP details: ")
print(f"IP: {ip}\nRegion: {region}\nCountry: {country}\nCity: {city}\nOrg.: {org}\n")
