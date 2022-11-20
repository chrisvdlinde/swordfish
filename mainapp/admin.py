from django.contrib import admin
from .models import Issue, Client, Type, Priority

@admin.register(Issue)
class IssueAdmin(admin.ModelAdmin):
	list_display = ['number']

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
	list_display = ['name']

@admin.register(Type)
class TypeAdmin(admin.ModelAdmin):
	list_display = ['name']

@admin.register(Priority)
class PriorityAdmin(admin.ModelAdmin):
	list_display = ['name']
