import requests
import json
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

def map_data_rows(table, result_type):
    # Extract the table rows
    rows = table.find_all('tr')

    attribute_names = RECORD_ATTRIBUTES[result_type]

    table_data = []
    for row in rows:
        cells = row.find_all('td')
        if len(cells) == len(attribute_names):
            row_data = {attribute_names[i]: cells[i].text.strip() for i in range(len(attribute_names))}
            table_data.append(row_data)

    return table_data

def process_wmc_url(result_type, url):
    response = open_url(url)
    
    if response.status_code == 200:
        # Parse the html request
        soup = BeautifulSoup(response.content, 'html.parser')

        # Get each table on the page
        tables = soup.find_all('table')

        # Print the number of tables on the page
        print('number of tables found: ' + str(len(tables)))

        # Calculate the index of the last table
        last_table_idx = len(tables) - 1
        result_table = tables[last_table_idx]

        # Map the data found in the last table on the page
        table_data = map_data_rows(result_table, result_type)

        # Convert the results to JSON
        table_json = json.dumps(table_data, indent=4)

        print(table_json)
    else:
        raise Exception("The response code was not 200")

    return table_json