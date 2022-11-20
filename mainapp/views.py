from django.shortcuts import render, redirect
from .forms import IssueForm, LabelForm
from .github import authorize, get_token, get_issues, add_issues, get_issue
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Issue, Client, Priority, Type
import requests
import json


# Create your views here.
def login(request):
    return render (request, 'mainapp/login.html')

# Re-direct to github login page
def github_auth(request):
    r = authorize()
    view = r.url
    return redirect(view)

# Get code and state for token generation and save token to session
def complete(request):
    code = request.GET.get('code')
    state = request.GET.get('state')
    print(code)
    print(state)

    r = get_token(state, code)
    if r == 'Incorrect State!':
        pass
    else:
       output = r.json()
       print(output)
       token = output['access_token']
       print(token)
       request.session['token'] = token

       return redirect('issues')

#Display current issues for repo
def issues(request):
    token = request.session.get('token')
    r = get_issues(token)
        
    for i in r:
        if len(i['labels']) > 0:
            for l in i['labels']:
                if l['name'].startswith('C:'):
                    if Client.objects.filter(name=l['name']).exists():
                        client = Client.objects.get(name=l['name'])
                    else:
                        client = Client.objects.create(name=l['name'])
                elif l['name'].startswith('P:'):
                    if Priority.objects.filter(name=l['name']).exists():
                        priority = Priority.objects.get(name=l['name'])
                    else:
                        priority = Priority.objects.create(name=l['name'])
                elif l['name'].startswith('T:'):
                    if Type.objects.filter(name=l['name']).exists():
                        type = Type.objects.get(name=l['name'])
                    else:
                        type = Type.objects.create(name=l['name'])
        
        number = i['number']
        title = i['title']
        desc = i['body_text']
        state = i['state']
        assignee = i['assignee']

        try:
            Issue.objects.create(number=number, title=title, description=desc,
            client=client, priority=priority, type=type, assigned_to=assignee, status=state)
        except:
            pass

        client = None
        priority = None
        type = None
    
        
    issues = Issue.objects.all()

    context = {'issues': issues}

    return render(request, 'mainapp/issues.html', context)

def create_issue(request):
    token = request.session.get('token')
    r = add_issues(token)
    context = {'create_issue' : r}
    if request.method == 'POST':
        form = IssueForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['issue_title']
            body = form.cleaned_data['description']
            url = 'https://api.github.com/repos/swordfishcode/gitintegration/issues'
            headers = {'Authorization': 'token {}'.format(token),
               'accept': 'application/vnd.github.VERSION.text+json',}
            params = {
                'owner' : 'swordfishcode',
                'repo' : 'gitintegration'
            }
            data = {
                'title' : title,
                'body' : body
            }
            r = requests.post(url=url, headers=headers, params=params, json=data)
            data = r.json()
            if r.status_code == 200:
                return redirect(issues)
            else:
                return 'Error generated'



    context['form'] = IssueForm()
    return render (request, 'mainapp/create_issue.html', context)



def add_label(request):
    token = request.session.get('token')
    print(token)
    context = {}
    if request.method == 'POST':
        form = LabelForm(request.POST)
        if form.is_valid():
            type = form.cleaned_data['type']
            priority = form.cleaned_data['priority']
            client = form.cleaned_data['client']
            issue_number = form.cleaned_data['issue_number']
            url = 'https://api.github.com/repos/swordfishcode/gitintegration/issues/%s/labels' % (issue_number)
            print(url) 
            headers = {'Authorization': 'token {}'.format(token),
                       'accept': 'application/vnd.github+json',}
            data = {"labels":["{%s}","{%s}","{%s}"]} % (client, priority, type)
            r = requests.post(url=url, headers=headers, json=data)
            data = r.json()
            print(r.status_code)
            print(data)
            if r.status_code == 200:
                return redirect(issues)
            else: 
                return 'Error generated'

    context['form'] = LabelForm()
    return render (request, 'mainapp/add_label.html', context)