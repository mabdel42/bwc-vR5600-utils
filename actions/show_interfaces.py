import requests
import warnings
import time
import json

from st2actions.runners.pythonrunner import Action

class showInterfaces(Action):
    def run(self, deviceIP, login, password):
        
        headers = {
            "accept": "application/json",
            "content-length": "0"
        }

        url_base = "https://" + deviceIP + "/rest/op/"
        url = url_base + "show/interfaces"

        print("\n")
        print("Sending REST call: POST " + url)

        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            cmd_response = requests.post(url, auth=(login, password), headers=headers, verify=False)
            cmd_response_code = cmd_response.status_code
            cmd_response_code = str(cmd_response_code)
            print("Response code: " + cmd_response_code)
        
            if cmd_response.status_code == 201:
                cmd_path = cmd_response.headers["Location"]
                url = "https://" + deviceIP + "/" + cmd_path
                print("Sending REST call: GET " + url)
                with warnings.catch_warnings():
                    warnings.simplefilter("ignore")
                    output_response = requests.get(url, auth=(login, password), headers=headers, verify=False)
                    cmd_response_code = cmd_response.status_code
                    cmd_response_code = str(cmd_response_code)
                    print("Response code: " + cmd_response_code)
                if output_response.status_code == 200:
                    print("\n")
                    print output_response.text