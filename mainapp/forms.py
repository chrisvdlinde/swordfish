from django import forms
#from .models import Type


#class NameForm(forms.Form):
    #your_name = forms.CharField(label='Your name', max_length=100)
    #type = forms.ModelChoiceField(queryset=Type.objects.all())


class IssueForm(forms.Form):
    issue_title = forms.CharField(label='Issue Title',max_length=50)
    description = forms.CharField(label='Description',max_length=50)


class LabelForm(forms.Form):
    type = forms.ChoiceField(choices=[('T: Bug', 'T: Bug'),('T: Enhancement', 'T: Enhancement'),('T: Support', 'T: Support')])
    priority = forms.ChoiceField(choices=[('P: High', 'P: High'),('P :Medium', 'P: Medium'),('P: Low', 'P: Low')])
    client = forms.ChoiceField(choices=[('C: Client AAA', 'C: Client AAA'),('C: Client ABC', 'C: Client ABC'),('C: Client MNO', 'C: Client MNO')])
    issue_number = forms.IntegerField(required=True)
