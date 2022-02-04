from http.server import BaseHTTPRequestHandler
from urllib import parse


class handler(BaseHTTPRequestHandler):

    def factorial(self, number):
 
        if number < 0:
            return 0
        elif number == 0 or number == 1:
            return 1
        else:
            fact = 1
            while(number > 1):
                fact *= number
                number -= 1
            return fact


    def do_GET(self):
        #res/header
        self.send_response(200)
        self.send_header('content-type', 'text/plain')
        self.end_headers()

        #do stuff
        s = self.path
        url_components = parse.urlsplit(s)
        query_dict = parse.parse_qs(url_components.query)

        number = query_dict.get("number")[0]
        number = int(number)

        self.wfile.write(f"factorial {number} is : ".encode())

        if number > 1:
            for i in range(number):
                self.wfile.write(f"\n{(self.factorial(i))}".encode())
        else:
            self.wfile.write(f"Error! Please enter a number!".encode())