from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import validate_email


class ContactForm(forms.Form):
    name = forms.CharField(label="Name", max_length=50)
    email = forms.CharField(label="Email Address", widget=forms.EmailInput)
    subject = forms.CharField(label="Subject", max_length=100)
    message = forms.CharField(
        label="Message",
        max_length=250,
        widget=forms.Textarea(attrs={"rows": 5, "cols": 60}),
    )

    def clean_name(self):
        name = self.cleaned_data["name"]
        if len(name) < 2:
            raise ValidationError("Name must be greater than 2 characters")
        if len(name) > 50:
            raise ValidationError("Name must be fewer than 50 characters")
        return name

    def clean_email(self):
        email = self.cleaned_data["email"]
        if email:
            try:
                validate_email(email)
            except:
                raise ValidationError("Invalid email address.")
        return email

    def clean_subject(self):
        subject = self.cleaned_data["subject"]
        if len(subject) < 2:
            raise ValidationError("Subject must be greater than 2 characters")
        if len(subject) > 50:
            raise ValidationError("Subject must be fewer than 50 characters")
        return subject

    def clean_message(self):
        message = self.cleaned_data["message"]
        if message:
            if len(message) >= 250:
                raise ValidationError("Message must be fewer than 250 characters.")
        return message
