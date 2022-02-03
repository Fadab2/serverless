  
 #This example uses Python 2.7 and the python-request library.
from http.server import BaseHTTPRequestHandler
from urllib import parse
import requests 

from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

url = 'pro-api.coinmarketcap.com'
parameters = {
  'start':'1',
  'limit':'5000',
  'convert':'USD'
}
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': '8257b809-17c1-4ed9-bb91-1e3441fa510e',
}

session = Session()
session.headers.update(headers)

try:
  response = session.get(url, params=parameters)
  data = json.loads(response.text)
  print(data)
except (ConnectionError, Timeout, TooManyRedirects) as e:
  print(e)