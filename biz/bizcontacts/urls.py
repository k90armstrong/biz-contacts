from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^dashboard/$', views.dashboard, name='index'),
    url(r'^signup/$', views.signup, name='index'),
    url(r'^login/$', views.login_view, name='index')    
]