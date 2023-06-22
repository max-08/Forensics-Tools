# Script IP-LOCATION - prende in input da un indirizzo IP mediante le API del servizio IPINFO, (con Token)
# restituisce la località dell'ip con coordinate

import ipinfo

import sys

try:
    ip_address = sys.argv[1]
except IndexError:
    ip_address = None
# inserire il token dal sito ipinfo.io
access_token = 'da inserire il token'
# crea un oggetto  con il token
handler = ipinfo.getHandler(access_token)
# indirizzo IP da geolocalizzare
details = handler.getDetails("DA INSERIRE INDIRIZZO IP")
# stampa le informazioni sotto forma di dizionario
for key, value in details.all.items():
    print(f"{key}: {value}")