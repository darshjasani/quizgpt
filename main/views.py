# quiz/views.py

import requests
from django.shortcuts import render, redirect
from django.views import View
from .models import PDF, QuizSettings, Question
from .forms import PDFUploadForm, QuizSettingsForm

class PDFUploadView(View):
    def get(self, request):
        form = PDFUploadForm()
        return render(request, 'main/upload.html', {'form': form})

    def post(self, request):
        form = PDFUploadForm(request.POST, request.FILES)
        if form.is_valid():
            pdf = form.save()
            return redirect('quiz_settings', pdf_id=pdf.id)
        return render(request, 'main/upload.html', {'form': form})

class QuizSettingsView(View):
    def get(self, request, pdf_id):
        pdf = PDF.objects.get(id=pdf_id)
        form = QuizSettingsForm()
        return render(request, 'main/settings.html', {'form': form, 'pdf': pdf})

    def post(self, request, pdf_id):
        pdf = PDF.objects.get(id=pdf_id)
        form = QuizSettingsForm(request.POST)
        if form.is_valid():
            settings = form.save(commit=False)
            settings.pdf = pdf
            settings.save()
            return redirect('quiz_results', pdf_id=pdf.id)
        return render(request, 'main/settings.html', {'form': form, 'pdf': pdf})

class QuizResultsView(View):
    def get(self, request, pdf_id):
        pdf = PDF.objects.get(id=pdf_id)
        settings = pdf.quizsettings
        questions = self.generate_questions(pdf, settings)
        return render(request, 'main/results.html', {'pdf': pdf, 'settings': settings, 'questions': questions})

    def generate_questions(self, pdf, settings):
        questions = []
        difficulty_levels = [
            ('easy', settings.easy_questions),
            ('medium', settings.medium_questions),
            ('hard', settings.hard_questions)
        ]

        for difficulty, count in difficulty_levels:
            if count > 0:
                # Replace this with your actual API call
                api_url = f"https://example-api.com/generate-questions?pdf_url={pdf.file.url}&difficulty={difficulty}&count={count}"
                response = requests.get(api_url)
                if response.status_code == 200:
                    api_questions = response.json()['questions']
                    for q in api_questions:
                        question = Question.objects.create(
                            pdf=pdf,
                            text=q['text'],
                            difficulty=difficulty,
                            options=q['options'],
                            correct_answer=q['correct_answer']
                        )
                        questions.append(question)

        return questions