from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^teacher-new/(?P<hash>\w+)/$', views.teacher_edit),
    url(r'^student-new/(?P<hash>\w+)/$', views.student_edit),
    url(r'^practice.png$', views.practice_png, name='lessons/practice_png'),
    url(r'^proficiency.png$', views.proficiency_png, name='lessons/proficiency_png')
]
