from django.contrib.auth.forms import forms
from .models import Review

class ReviewCreationForm(forms.ModelForm):
    
    class Meta:
        model = Review
        # fields = ()
        exclude = ('user', 'movie')