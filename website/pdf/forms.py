"""
Form for Handling User input.
"""
from django import forms
from pdf.models import Resume

class ResumeForm(forms.ModelForm):
    """Generating a form based of Resume model."""
    class Meta:
        model = Resume
        fields = ["full_name",
                  "email",
                  "summary",
                  "degree",
                  "education",
                  "experience",
                  "skills"
                  ]
    def __init__(self, *args, **kwargs):
        super(ResumeForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'  # Bootstrap class for inputs
            field.widget.attrs['placeholder'] = f'Enter your {field.label}'