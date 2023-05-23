from http.server import BaseHTTPRequestHandler
from urllib import parse
import requests

class handler(BaseHTTPRequestHandler):
    """
    Custom request handler class that handles HTTP GET requests and retrieves country-capital information.
    """

    def do_GET(self):
        """
        Handles the HTTP GET request and retrieves the country-capital information based on query parameters.

        If the 'country' parameter is provided, it retrieves the capital of the specified country.
        If the 'capital' parameter is provided, it retrieves the country associated with the specified capital.
        If neither parameter is provided, it indicates that a capital or country should be provided.

        The retrieved country-capital information is sent as the response.

        Returns:
            None
        """
        s = self.path
        url_components = parse.urlsplit(s)
        query_string_list = parse.parse_qsl(url_components.query)
        given_dictionary = dict(query_string_list)
        country = given_dictionary.get('country')
        capital = given_dictionary.get('capital')
        if country:
            country_url = f'https://restcountries.com/v3.1/name/{country}'
            req = requests.get(country_url)
            data = req.json()
            capital_name = data[0]['capital'][0]
            retrieved_capital = f'The capital of {country.title()} is {capital_name}'

        elif capital:
            capital_url = f'https://restcountries.com/v3.1/capital/{capital}'
            req = requests.get(capital_url)
            data = req.json()
            country_name = data[0]['name']['common']
            retrieved_capital = f'{capital.title()} is the capital of {country_name}'
        else:
            retrieved_capital = "Please provide a capital or country."

        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(retrieved_capital.encode())
        return
