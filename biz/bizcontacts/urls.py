from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^dashboard/$', views.dashboard, name='dashboard'),
    url(r'^dashboard/search/$', views.dashboard_search, name='dashboard_search'),    
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^login/$', views.login_view, name='login'),    
    url(r'^logout/$', views.logout_view, name='logout'),
    url(r'^dashboard/newcontact/$', views.create_contact, name='create_contact')    
]
