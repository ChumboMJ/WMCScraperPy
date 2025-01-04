import requests
from bs4 import BeautifulSoup
from requests.exceptions import HTTPError
from .constants import RESULTS_TYPE, RECORD_ATTRIBUTES, BROWSER_REQ_HEADER

def open_url(url):
    try:
        #Send a GET request to the given url
        response = requests.get(url, headers=BROWSER_REQ_HEADER)
        # Raise an HTTPError for bad responses (4xx and 5xx)
        response.raise_for_status()
    except HTTPError as http_err:
        raise HTTPError(f"HTTP error occurred: {http_err}")
    except Exception as err:
        raise Exception(f"Other error occurred: {err}")
    
    return response

def process_wmc_url(result_type, url):
    response = open_url(url)
    
    if response.status_code == 200:
        # Parse the html request
        soup = BeautifulSoup(response.content, 'html.parser')

        # Get each table on the page
        tables = soup.find_all('table')

        # Print the number of tables on the page
        print('number of tables found: ' + str(len(tables)))

        lastTable = len(tables) - 1
        resultTable = tables[lastTable]

    return "Hello World"