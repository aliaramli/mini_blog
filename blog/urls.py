from . import views
from django.urls import path
from register import views as rv

urlpatterns = [ 
#   path ('', views.PostList.as_view(), name='home'),
   path ('', views.postlist, name='home'),
   path('register/', rv.register, name="register"),
   path('blog/create/', views.userposts_create_view, name='userposts_create_view'),
   path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
   path('tag/<slug:slug>/', views.tagged, name="tagged"),

 ]
