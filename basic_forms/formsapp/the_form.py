from django import forms
from django.core import validators
class My_Form(forms.Form):

    name = forms.CharField()
    email = forms.EmailField()
    verify_email = forms.EmailField(label = "Re-enter Email: ")
    text = forms.CharField(widget = forms.Textarea)

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data['email']
        v_email = cleaned_data['verify_email']

        if email != v_email:
            raise forms.ValidationError(("Emails didn't Match!"), code = 'mismatch')
