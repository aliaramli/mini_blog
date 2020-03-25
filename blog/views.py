from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Post
from taggit.models import Tag

# Create your views here.
class PostList(generic.ListView):
    queryset = Post.objects.filter(status=2).order_by('-created_on')
    template_name = 'index.html'

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'

def tagged(request, slug):
    tag = get_object_or_404(Tag, slug=slug)
    # Filter posts by tag name  
    posts = Post.objects.filter(tags=tag)
    context = {
        'tag':tag,
        'post_list':posts,
    }
    return render(request, 'index.html', context)

