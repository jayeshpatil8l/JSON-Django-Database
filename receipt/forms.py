from django import forms

class uploadJSONFile(forms.Form):
    json_file = forms.FileField(label = 'Upload JSON here')
    