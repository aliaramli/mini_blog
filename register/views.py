from django.shortcuts import render, redirect, get_object_or_404 
from .forms import RegisterForm
from django.views import generic
from blog.models import User

# Create your views here.
def register(response):
    if response.method == "POST":
       form = RegisterForm(response.POST)
       if form.is_valid():
          form.save()
       return redirect("")
    else:
        form = RegisterForm()
    return render(response, "register/register.html", {"form":form})

class UserProfile(generic.DetailView):
    model = User
    template_name = 'registration/profile.html'
    def get_object(self):
        return get_object_or_404(User, username=self.request.user.username)
