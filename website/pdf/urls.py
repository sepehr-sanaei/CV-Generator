"""
Url mapping for pdf app.
"""
from django.urls import path

from pdf.views import ResumeCreateView, ResumeTemplateView, ResumeListView

app_name = "pdf"

urlpatterns = [
    path("", ResumeListView.as_view(), name="resume-list"),
    path("resume-create", ResumeCreateView.as_view(), name="resume-create"),
    path("resume/<int:pk>/", ResumeTemplateView.as_view(), name="resume-detail"),
]