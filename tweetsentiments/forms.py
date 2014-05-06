from django import forms

class KeyForm(forms.Form):
    keyword = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'placeholder': 'Enter the keyword to search Tweet'}))