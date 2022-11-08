import requests
import json
from urllib.parse import urljoin
from decouple import config

id = config('ID')
secret = config('SECRET')
git_state = config('GIT_STATE')



def authorize():
    url = 'https://github.com/login/oauth/authorize'
    parameters = {
        'client_id' : id,
        'redirect_uri' : 'https://ec2-44-210-115-253.compute-1.amazonaws.com:8150/complete',
        'scope': 'repo',
        'state': git_state,
        'allow_signup' : 'false'
    }

    response = requests.get(url=url,params=parameters)
    
    return response


def get_token(state, code):
    if state != git_state:
        return 'Incorrect State!'

    url = 'https://github.com/login/oauth/access_token'
    parameters = {
        'client_id' : id,
        'client_secret' : secret,
        'code' : code,
        'redirect_uri' : 'https://ec2-44-210-115-253.compute-1.amazonaws.com:8150/complete',
    }

    header = {'Accept' : 'application/json'}

    response = requests.post(url=url,params=parameters, headers=header)
    

    return response

def get_issues(token):
    url = 'https://api.github.com/repos/swordfishcode/gitintegration/issues'
    headers = {'Authorization': 'token {}'.format(token),
               'Accept': 'application/vnd.github.VERSION.text+json'}

    response = requests.get(url,headers=headers)
    #print(response.status_code)
    data = response.json()
    #print(data)

    return data



def add_issues(token):
    url = 'https://api.github.com/repos/swordfishcode/gitintegration/issues'
    headers = {'Authorization': 'token {}'.format(token),
               'Accept': 'application/vnd.github.VERSION.text+json',
                'Owner' : 'swordfishcode',
                'Repo' : 'gitintegration',
                'Title' : 'placeholder',
                'Body' : 'placeholder'}

    r = requests.post(url=url, headers=headers)
    data = r.json()