import azure.functions as func
import datetime
import json
import logging

app = func.FunctionApp()

@app.route(route="ScrapeWmcData", auth_level=func.AuthLevel.FUNCTION)
def ScrapeWmcData(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    # Retrieve the 'results_type' query parameter from the request URL
    name = req.params.get('results_type')

    # TODO: Validate that the results_type is in the RESULTS_TYPE constant

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
        # TODO: Process the link to get the Tsble JSON
        # TODO: Write the JSON data out to CosmosDB

        return func.HttpResponse(f"Here is the target_link value: {target_link}. This HTTP triggered function executed successfully.")
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Be sure to pass a target link for a customized response",
             status_code=200
        )