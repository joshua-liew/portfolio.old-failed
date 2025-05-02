from django import forms
from django.utils.translation import gettext_lazy as _


class ContactForm(forms.Form):
    name = forms.CharField(required=True, max_length=30, strip=True, label=_("Name"))
    email = forms.EmailField(required=True, widget=forms.EmailInput, label=_("Email"))
    subject = forms.CharField(required=True, max_length=50, label=_("Subject/Purpose"))
    text = forms.CharField(required=True, widget=forms.Textarea, label=_("Message"))

    name.widget.attrs.update({
        "aria-label": "name",
        "id": "name",
        "required": True,
        "placeholder": _("Joshua Liew"),
    })
    email.widget.attrs.update({
        "aria-label": "email",
        "id": "email",
        "required": True,
        "placeholder": "name@example.com",
    })
    subject.widget.attrs.update({
        "aria-label": "subject",
        "id": "subject",
        "required": True,
        "placeholder": _("Inquiry - Design Website for NGO"),
    })
    text.widget.attrs.update({
        "aria-label": "text",
        "id": "text",
    })