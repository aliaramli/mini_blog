from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Post, Coronavirus, Preference
from taggit.models import Tag
import taggit
from .form import CustomForm, CommentForm, CustomUserBlogPostForm
from datetime import datetime
from django.http import HttpResponseRedirect
from django.core.files.storage import FileSystemStorage
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)

def postlist(request):
    post = Post.objects.filter(status=2).order_by('-created_on')
    template_name = 'index.html'
    corona = Coronavirus().get_data()
    context = {'post_list':post,
               'corona': corona,
              }
    return render(request, 'index.html', context)


def post_detail(request, slug):
    template_name = 'post_detail.html'
    corona = Coronavirus().get_data()
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.filter(active=True)
    preferences = post.preferences.filter(value=1)
    new_comment = None
    error_message = None
    logger.error(request.POST)
    comment_form = CommentForm()
    
    if request.method == 'POST' and  not request.POST.get('value'):
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.author = request.user
            new_comment.save()
    
    elif request.method == 'POST' and request.POST.get('value'):   
        if not request.user.is_authenticated:
            error_message = "You need to login first"
        else:
            existing_preference = Preference.objects.filter(author=request.user)
            if not existing_preference:
                preference = Preference()
                preference.author = request.user
                preference.post = post
                preference.value = request.POST.get('value')
                preference.save()
            else :
                error_message = "You have liked before!"
     
   
    return render(request, template_name, {'post': post,
                                           'comments': comments,
                                           'new_comment': new_comment,
                                           'comment_form': comment_form,
                                           'corona':corona,
                                           'preferences':preferences,
                                           'error_message': error_message})

def tagged(request, slug):
    tag = get_object_or_404(Tag, slug=slug)
    # Filter posts by tag name  
    posts = Post.objects.filter(tags=tag)
    context = {
        'tag':tag,
        'post_list':posts,
    }
    return render(request, 'index.html', context)


def userposts_create_view(request):
    form = CustomUserBlogPostForm(request.POST or None)
    logger.error(request.FILES)
    if request.method == "POST":
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = datetime.now()
            post.status = 1
            logger.error(request.POST)
            cover = request.FILES.get('cover')
            if cover:
                fs = FileSystemStorage()
                filename = fs.save(cover.name, cover)
                logger.error(cover.name)
                post.cover = cover.name
            post.save()
            tags = request.POST.get('tags')
            tag_list = taggit.utils._parse_tags(tags)
            post.tags.add(*tag_list)
            post.save()         
        return HttpResponseRedirect("/accounts/profile") 
    context = {'form':form,}
    return render(request, 'create-post-view.html',context)


