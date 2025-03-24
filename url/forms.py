from django import forms

class Url(forms.Form):
    url = forms.CharField(label="URL", widget=forms.TextInput(attrs={'placeholder': 'Enter your URL'}))
    use_alias = forms.BooleanField(
        label="Use custom alias?",
        required=False, 
        initial=False,
        widget=forms.CheckboxInput(attrs={'id': 'use_alias',"default" : "False"})
    )
    custom_slug = forms.CharField(
        label="Custom Alias",
        max_length=15,
        required=False,
        widget=forms.TextInput(attrs = {"placeholder" : 'Enter custom alias'})
    )