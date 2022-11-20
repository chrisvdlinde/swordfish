import requests
import json
from urllib.parse import urljoin
from django.conf import settings

ID = settings.ID
SECRET = settings.SECRET
GIT_STATE = settings.GIT_STATE



def authorize():
    url = 'https://github.com/login/oauth/authorize'
    parameters = {
        'client_id' : ID,
        'redirect_uri' : 'http://localhost:8000/complete',
        'scope': 'repo',
        'state': GIT_STATE,
        'allow_signup' : 'false'
    }

    response = requests.get(url=url,params=parameters)
    print(response.status_code)
    
    return response


def get_token(state, code):
    if state != GIT_STATE:
        return 'Incorrect State!'

    url = 'https://github.com/login/oauth/access_token'
    parameters = {
        'client_id' : ID,
        'client_secret' : SECRET,
        'code' : code,
        'redirect_uri' : 'http://localhost:8000/complete',
    }

    header = {'Accept' : 'application/json'}

    response = requests.post(url=url,params=parameters, headers=header)
    print(response.status_code)
    

    return response

def get_issues(token):
    url = 'https://api.github.com/repos/chrisvdlinde/issues/issues'
    headers = {'Authorization': 'token {}'.format(token),
               'Accept': 'application/vnd.github.VERSION.text+json'}

    response = requests.get(url,headers=headers)
    #print(response.status_code)
    if response.status_code == 200:
        data = response.json()
    #print(data)

        return data

    else: 
        return 'You are not authorized to view this page'

def get_issue(url, token):
    headers = {'Authorization': 'token {}'.format(token),
               'Accept': 'application/vnd.github.VERSION.text+json'}

    r = requests.get(url,headers=headers)
    
    return r.json()

"""
def get_labels(url, token):
    url = url.replace('{/name}', '')
    headers = {'Authorization': 'token {}'.format(token),
               'Accept': 'application/vnd.github.VERSION.text+json'}

    r = requests.get(url,headers=headers)
    
    return r.json()
"""

def add_issues(token):
    url = 'https://api.github.com/repos/chrisvdlinde/issues/issues'
    headers = {'Authorization': 'token {}'.format(token),
               'Accept': 'application/vnd.github.VERSION.text+json',
                'Owner' : 'swordfishcode',
                'Repo' : 'gitintegration',
                'Title' : 'placeholder',
                'Body' : 'placeholder'}

    r = requests.post(url=url, headers=headers)
    data = r.json()