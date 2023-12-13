from django.forms import ModelForm

from .models import contactTable

# from django.forms import forms

class contactForm(ModelForm):
    class Meta:
        model= contactTable
        fields = ['name', 'email', 'phone', 'message']
    
    def __init__(self, *args, **kwargs):
        super(contactForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class':'form-control', 'placeholder':'name'})
        self.fields['email'].widget.attrs.update({'class':'form-control', 'placeholder':'email'})
        self.fields['phone'].widget.attrs.update({'class':'form-control', 'placeholder':'phone number'})
        self.fields['message'].widget.attrs.update({'class':'form-control', 'placeholder':'Message'})