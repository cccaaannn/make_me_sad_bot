import requests
import json
import sys
import os

class currency_api:
    def __init__(self) -> None:
        api_key_env_path = "CURRENCY_API_KEY"
        try:
            self.api_key = os.environ[api_key_env_path]
            self.url = "https://v6.exchangerate-api.com/v6/" + self.api_key + "/latest/USD"
        except:
            print("Could not get the api key from {0}".format(api_key_env_path))
            sys.exit()  

    def request_to_api(self):
        result = requests.get(self.url, verify=False).text
        return json.loads(result)["conversion_rates"]["TRY"]
