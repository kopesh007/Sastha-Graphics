from django import forms

class ContactForm(forms.Form):
    name=forms.CharField(max_length=50,label="Name",required=True)
    email=forms.EmailField(label="Email",required=True)
    number=forms.CharField(label="Number",required=True,max_length=10,min_length=10)
    interest=forms.CharField(label="Message",max_length=500)
