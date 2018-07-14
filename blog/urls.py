from django.urls import path
from django.conf.urls import url
from . import views


app_name = 'blog'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),

    #url('^post/(?P<pk>[0-9])+/$',views.detail, name='detail'),
    path('post/<int:pk>/',views.detail, name='detail'),
    path('archives/<int:year>/<int:month>/', views.archives, name='archives'),
    path('category/<int:pk>/', views.category, name='category'),
    path('tag/<int:pk>/', views.tag, name='tag'),


    path('about.html', views.about, name='about'),
    path('index.html', views.IndexView.as_view(),name='index'),
    path('fullwidth.html', views.fullwidth, name='fullwidth'),
    path('contact.html', views.contact, name='contact')

]