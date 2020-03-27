from . import views
from django.conf.urls import url
from django.urls import path
from register import views as rv

urlpatterns = [ 
   path ('', views.postlist, name='home'),
   path('register/', rv.register, name="register"),
   path('blog/create/', views.userposts_create_view, name='userposts_create_view'),
   path('<slug:slug>/', views.post_detail, name='post_detail'),
   path('tag/<slug:slug>/', views.tagged, name="tagged"),
 ]
