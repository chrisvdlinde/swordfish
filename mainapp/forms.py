from django import forms
#from .models import Type


#class NameForm(forms.Form):
    #your_name = forms.CharField(label='Your name', max_length=100)
    #type = forms.ModelChoiceField(queryset=Type.objects.all())


class IssueForm(forms.Form):
    issue_title = forms.CharField(label='Issue Title',max_length=50)
    description = forms.CharField(label='Description',max_length=50)


class LabelForm(forms.Form):
    type = forms.CharField(label='Issue Type',max_length=20)
    priority = forms.CharField(label='Issue Priority',max_length=20)
    client = forms.CharField(label='Issue Client',max_length=20)
