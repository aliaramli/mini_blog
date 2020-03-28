import django.forms as forms
from .models import Post,Comment
class CustomForm(forms.ModelForm):
    content = forms.CharField(strip=False, widget=forms.Textarea)

    class Meta:
        model = Post
        exclude = []
        fields = ('title', 'slug','cover','content','tags', 'status') 

class CustomUserBlogPostForm(forms.ModelForm):
    content = forms.CharField(strip=False, widget=forms.Textarea)

    class Meta:
        model = Post
        exclude = []
        fields = ('title', 'slug','cover','content','tags') 

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)

