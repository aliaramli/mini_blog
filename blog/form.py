import django.forms as forms
from .models import Post
class CustomForm(forms.ModelForm):
    content = forms.CharField(strip=False, widget=forms.Textarea)

    class Meta:
        model = Post
        exclude = []

