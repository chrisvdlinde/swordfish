"""githublogin URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from mainapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.login, name='login'),
    path('authorize', views.github_auth, name='authorize'),
    path('complete', views.complete, name='complete'),
    path('issues', views.issues, name='issues'),
    path('create_issue', views.create_issue, name='create_issue'),
    path('add_label', views.add_label, name='add_label'),
    path('api-auth/', include('rest_framework.urls'))
]
