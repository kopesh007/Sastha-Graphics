from django import forms

class ContactForm(forms.Form):
    name=forms.CharField(max_length=50,label="name",required=True)
    email=forms.EmailField(label="email",required=True)
    interest=forms.CharField(label="interest",max_length=500)
