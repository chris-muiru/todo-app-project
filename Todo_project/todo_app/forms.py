from django import  forms
class user_form(forms.Form):
    task=forms.CharField(max_length=200, widget= forms.TextInput
                           (attrs={'placeholder':'Enter Task'}))
    start=forms.DateTimeField(widget= forms.TextInput
                           (attrs={'placeholder':'Start: YYYY-mm-dd HH:MM:SS'}))
    finish=forms.DateTimeField(widget= forms.TextInput
                           (attrs={'placeholder':'Start: YYYY-mm-dd HH:MM:SS'}))

