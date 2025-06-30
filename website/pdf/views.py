"""
Views for processing User request for generating a cv.
"""
from django.db.models.query import QuerySet
from django.views.generic import FormView, DetailView, ListView
from django.urls import reverse_lazy
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.mixins import LoginRequiredMixin

from pdf.models import Resume
from pdf.forms import ResumeForm


import pdfkit


class ResumeCreateView(LoginRequiredMixin, FormView):
    """View for creating a resume based of user input."""
    template_name = "pdf/resume.html"
    form_class = ResumeForm
    success_url = reverse_lazy("pdf:resume-list")

    def form_valid(self, form):
        """Validate the data in the form."""
        form.instance.user = self.request.user
        form.save()
        return super().form_valid(form)


class ResumeListView(LoginRequiredMixin, ListView):
    """A view for listing all the CVs that a user have made."""
    model = Resume
    template_name = "pdf/resume-list.html"
    context_object_name = "resumes"

    def get_queryset(self):
        """Filter the resumes by the user."""
        return Resume.objects.filter(user=self.request.user)

class ResumeTemplateView(LoginRequiredMixin, DetailView):
    """View for showing the information of the user and generating a resume as a PDF."""
    model = Resume
    template_name = "pdf/cv.html"
    context_object_name = "user_profile"

    def get(self, request, *args, **kwargs):
        # Fetch the user profile object
        user_profile = self.get_object()

        # Render the HTML template
        template = self.get_template_names()[0]  # Fetch template path
        html = loader.render_to_string(template, {'user_profile': user_profile})

        # Set PDF options
        options = {
            'page-size': 'Letter',
            'encoding': 'UTF-8',
        }

        # Convert HTML to PDF
        pdf = pdfkit.from_string(html, False, options)

        # Create an HTTP response with the generated PDF
        response = HttpResponse(pdf, content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="resume.pdf"'

        return response
