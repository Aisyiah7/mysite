from django.conf.urls import url

from . import views

urlpatterns = [
    #Login/logout urls
    url(r'^login/$','django.contrib.auth.views.login', {'template_name': 'login.html'}),
    url(r'^logout/$','django.contrib.autj.views.logout', {'next_page': '/login/'}),
    url(r'^$', views.index, name='index'),
]
