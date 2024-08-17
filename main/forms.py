# quiz/forms.py

from django import forms
from .models import PDF, QuizSettings

class PDFUploadForm(forms.ModelForm):
    class Meta:
        model = PDF
        fields = ['file']

class QuizSettingsForm(forms.ModelForm):
    class Meta:
        model = QuizSettings
        fields = ['easy_questions', 'medium_questions', 'hard_questions']
        widgets = {
            'easy_questions': forms.NumberInput(attrs={'type': 'range', 'min': 0, 'max': 25}),
            'medium_questions': forms.NumberInput(attrs={'type': 'range', 'min': 0, 'max': 25}),
            'hard_questions': forms.NumberInput(attrs={'type': 'range', 'min': 0, 'max': 25}),
        }