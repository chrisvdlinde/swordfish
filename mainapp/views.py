from django.shortcuts import render, redirect
from .forms import IssueForm
from .github import authorize, get_token, get_issues, add_issues
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Issue
import requests


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

    r = get_token(state, code)
    if r == 'Incorrect State!':
        pass
    else:
       output = r.json()
       token = output['access_token']
       request.session['token'] = token

       return redirect('issues')

#Display current issues for repo
def issues(request):
    token = request.session.get('token')
    r = get_issues(token)
    context = {'issues': r}
    
    for i in r:
        issue_data = Issue (
            number = i['number'],
            title = i['title'],
            description = i['body_text'],
        )


            
        issue_data.save()
        #Issue = Issue.objects.all()


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
            print(r.status_code)
            print(data)


    context['form'] = IssueForm()
    return render (request, 'mainapp/create_issue.html', context)