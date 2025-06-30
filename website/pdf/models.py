"""
models for pdf.
"""
from django.db import models
from django.contrib.auth import get_user_model

class Resume(models.Model):
    """A model class for user information."""
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    full_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    summary = models.TextField()
    degree = models.CharField(max_length=255)
    education = models.CharField(max_length=255)
    experience = models.TextField()
    skills = models.TextField()

    def __str__(self):
        """Return the string representation of model."""
        return f"{self.user.email}'s CV Profile"

