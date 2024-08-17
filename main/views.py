# quiz/views.py

from django.shortcuts import render, redirect
from django.views import View
from .models import PDF, QuizSettings
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
        return render(request, 'main/results.html', {'pdf': pdf, 'settings': settings})