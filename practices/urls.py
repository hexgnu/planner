from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='practices/index'),
    url(r'^finish/$', views.finish, name='practices/finish'),
    url(r'^time/$', views.create_timer, name='practices/create_timer')
]
