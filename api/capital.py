# from http.server import BaseHTTPRequestHandler
# from urllib import parse 
# import requests

# class handler(BaseHTTPRequestHandler):

#     def do_GET(self):
#         """
#         Custom request handler class that handles HTTP GET requests and retrieves country-capital information.
#         """
#         s=self.path
#         url_components=parse.urlsplit(s)
#         query_string_list = parse.parse_qsl(url_components.query)
#         dictionary=dict(query_string_list)
        
#         if 'country' in dictionary:
#             country=dictionary['country']
#             url = 'https://restcountries.com/v3.1/name/'
#             r = requests.get(url + country)
#             data = r.json()
                
#             capital = str(data[0]['capital'][0])
#             message = f'the capital of {country} is {capital}.' 

#         elif 'capital' in dictionary:
#             capital=dictionary['capital']
#             url = 'https://restcountries.com/v3.1/capital/'
#             r = requests.get(url + capital)
#             data = r.json()
#             country=str(data[0]['name']['common'])
#             message=f'{capital} is the capital of {country}.'
#         else :
#             message="write country or capital in the url."

#         self.send_response(200)
#         self.send_header('Content-type','text/plain')
#         self.end_headers()
     
#         self.wfile.write(message.encode())
#         return
from http.server import BaseHTTPRequestHandler
from urllib import parse
import requests
 
class handler(BaseHTTPRequestHandler):

    # method to handle HTTP GET Request 
    def do_GET(self):
        """Respond to a GET request."""
        s = self.path
        url_components = parse.urlsplit(s)
        query_strings_list = parse.parse_qsl(url_components.query)
        dic = dict(query_strings_list)
        country = dic.get("country")
        capital = dic.get("capital")
        result = ""

        if country:
            url = f"https://restcountries.com/v3.1/name/{country}"
            
            try:
                res = requests.get(url)
                data = res.json()
                capital_res = data[0]["capital"][0]
                result = f"The capital of {country} is {capital_res}"
            except:
                result = "Country not found"
            
        if capital:
            url = f"https://restcountries.com/v3.1/capital/{capital}"
            
            try:
                res = requests.get(url)
                data = res.json()
                country_res = data[0]["name"]["common"]
                result = f"{capital}is the capital of {country}."
            except:
                result = "Capital not found"
       
        
        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()
        self.wfile.write(result.encode('utf-8'))
        return