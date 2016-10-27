import requests
import warnings
import time
import json

from st2actions.runners.pythonrunner import Action

class delInterface(Action):
    def run(self, deviceIP, login, password, cmd_path, intfType, intfNum):
        
        headers = {
            "accept": "application/json",
            "content-length": "0"
        }

        url_base = "https://" + deviceIP + "/" + cmd_path
        url = url_base + "/delete/interfaces/" + intfType + "/" + intfNum

        print("\n")
        print("Sending REST call: PUT " + url)

        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            cmd_response = requests.put(url, auth=(login, password), headers=headers, verify=False)
            cmd_response_code = cmd_response.status_code
            cmd_response_code = str(cmd_response_code)
            print("Response code: " + cmd_response_code)
        
        try:
            data = json.loads(cmd_response.text)
            print("Response body: ")
            print json.dumps(data, sort_keys=True, indent=4)
        except:
            print ("Response body is empty")