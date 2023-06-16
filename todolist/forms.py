from django import forms

class Todolistform(forms.Form):
    text = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'input_to_the_form', 'placeholder':'Enter todo e.g. Wash my car'}))