import json
import pandas as pd
import numpy as np
import requests



def lambda_handler(event, context):
    pandas_version = pd.__version__
    numpy_version = np.__version__
    
    # Ping nkstudios.com and get the status code
    response = requests.get("https://www.w3schools.com/")
    w3schools_status = response.status_code
    
    # Construct the return statement
    return_statement =f"Pandas Version: {pandas_version}, Numpy Version {numpy_version}, \
W3schools Request status: {w3schools_status}"

    # Set the return statement expected by AWS Lambda
    return {
        'statusCode':200,
        'body': json.dumps(return_statement)
    }