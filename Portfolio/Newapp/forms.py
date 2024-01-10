from django import forms
from Newapp.models import Resume

class ResumeForm(forms.ModelForm):
    class Meta:
        model = Resume
        fields = ['file']