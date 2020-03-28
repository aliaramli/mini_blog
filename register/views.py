from django.shortcuts import render, redirect, get_object_or_404 
from .forms import RegisterForm
from django.views import generic
from blog.models import CustomUser, Post, STATUS, Preference
# Create your views here.
def register(response):
    if response.method == "POST":
       form = RegisterForm(response.POST)
       if form.is_valid():
          user = form.save(commit=False)
          user.is_active = False
          form.save()
       return redirect("/accounts/login")
    else:
        form = RegisterForm()
    return render(response, "register/register.html", {"form":form})

class UserProfile(generic.DetailView):
    model = CustomUser
    template_name = 'registration/profile.html'
    def get_object(self):
        return get_object_or_404(CustomUser, username=self.request.user.username)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        posts = Post.objects.filter(author=self.request.user.id)
        liked_posts = Preference.objects.filter(value=1, author=self.request.user.id)
        context['post_list'] = posts 
        context['status'] = STATUS
        context['liked_posts'] = liked_posts
        return context



