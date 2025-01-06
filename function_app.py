import azure.functions as func
import datetime
import json
import logging
from dataprocessing import is_valid_result_type, process_wmc_url

app = func.FunctionApp()

@app.route(route="ScrapeWmcData", auth_level=func.AuthLevel.FUNCTION)
def ScrapeWmcData(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    # Retrieve the 'results_type' query parameter from the request URL
    results_type = req.params.get('results_type')

    if results_type is None:
        return func.HttpResponse(
            'results_type must have a value',
            status_code=400)

    if not is_valid_result_type(results_type):
        return func.HttpResponse(
            'results_type invalid. Must be 1 (PAX), 2 (RAW), or 3 (LAP)',
            status_code=400)

    try:
        req_body = req.get_json()
    except ValueError:
        return func.HttpResponse(
            "Invalid JSON in request body",
            status_code=400
        )
    else:
        target_link = req_body.get('target_link')

    if target_link:
        results_json = process_wmc_url(results_type, target_link)
        print(results_json)

        # TODO: Write the JSON data out to CosmosDB

        return func.HttpResponse(f"Here is the target_link value: {target_link}. This HTTP triggered function executed successfully.")
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Be sure to pass a target link for a customized response",
             status_code=200
        )