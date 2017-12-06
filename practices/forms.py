from django import forms

from .models import Practice

class FinishPracticeForm(forms.ModelForm):
    class Meta:
        model = Practice
        fields = ('finished',)
