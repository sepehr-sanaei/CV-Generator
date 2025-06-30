"""
Admin Panel configuration for Profile model.
"""
from django.contrib import admin
from pdf.models import Resume

admin.site.register(Resume)