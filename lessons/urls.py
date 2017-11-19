from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^teacher-new/(?P<hash>\w+)/$', views.teacher_edit),
    url(r'^student-new/(?P<hash>\w+)/$', views.student_edit),
    url(r'^progress.png$', views.progress_png, name='lessons/progress_png')
]
