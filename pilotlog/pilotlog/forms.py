from django import forms


class ImportForm(forms.Form):
    pilot_log = forms.FileField()
