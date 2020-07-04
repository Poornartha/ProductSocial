from django import forms

class UploadFileForm(forms.Form):
	image = forms.ImageField()

class GetSearch(forms.Form):
	search = forms.CharField(max_length=100)
