import requests
import json

def GetSolCallBackRequest(i):
    payload={'salesOrderNo':i,'lineStatus':'20'}
    return payload


def Sol_callback(req):
    callbackUrl='http://localhost:8000/sol/provision/complete'
    response = requests.post(url=callbackUrl, data=json.dumps(req), headers={'Content-type': 'application/json'})
    return response.json()

