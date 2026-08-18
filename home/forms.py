from django import forms
from .models import Convertion

class OldLinkForm(forms.ModelForm):
    class Meta:
        model = Convertion
        fields = ['old_link']