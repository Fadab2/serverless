import re
from dotenv import load_dotenv
load_dotenv()
import os
from http.server import BaseHTTPRequestHandler
from urllib import parse
import requests 


class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        API_KEY = os.getenv("API_KEY")
        
        
        url_path = self.path
        url_components = parse.urlsplit(url_path)
        query_string_list = parse.parse_qsl(url_components.query)
        city_data = dict(query_string_list)

        if "city_name" in city_data:

            url = f'https://api.weatherbit.io/v2.0/current?lat=35.7796&lon=-78.6382&key={API_KEY}&include=minutely'
            r = requests.get(url + city_data['city_name'])

            data = r.json()
            cities = []
            for city in data:
                weather = city["data"]["city_name"]
                cities.append(weather)
            message = str(cities)
        else:
            message = "Please enter a valid city name"
       
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()

        self.wfile.write(message.encode())

        return
        #city_name = [11]