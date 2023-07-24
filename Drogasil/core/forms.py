from django import forms

class PesquisaForm(forms.Form):
    search = forms.CharField(widget=forms.HiddenInput(), required=True)