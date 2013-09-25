from django import forms 

class ContactForm(forms.Form):
	nom = forms.CharField(required=False)
	tel = forms.IntegerField(required=False)
	email = forms.EmailField()
	message = forms.CharField(widget = forms.Textarea)