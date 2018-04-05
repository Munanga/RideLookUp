from django import forms
from AppAuto.models import Vehicle,ContactModel

class VehicleModelForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = "__all__"

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactModel
        fields = "__all__"