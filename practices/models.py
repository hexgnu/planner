from django.db import models

from lessons.models import Lesson, HomeworkItem

class Practice(models.Model):
    finished = models.BooleanField(default=False)
    lesson = models.ForeignKey(Lesson, blank=False)
    homework_item_timers = models.ForeignKey('HomeworkItemTimer')

class HomeworkItemTimer(models.Model):
    homework_item = models.ForeignKey(HomeworkItem, blank=False)
    practice_session = models.ForeignKey('Practice', blank=False)
    seconds = models.PositiveIntegerField()
