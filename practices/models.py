from django.db import models

from lessons.models import Lesson, HomeworkItem

class Practice(models.Model):
    finished = models.BooleanField(default=False)
    lesson = models.ForeignKey(Lesson, blank=False)

    def plan(self):
        homework_item_timers = []

        session_map = {
                0: [1],
                1: [1,2],
                2: [1,3],
                3: [1,2,4]
        }

        min_proficiency = min([hi.proficiency for hi in self.lesson.homework_items.all()])

        session = (self.lesson.practice_set.count()-1) % 4

        for hi in self.lesson.homework_items.all():
            if hi.proficiency < 5 and (hi.proficiency - min_proficiency + 1) in session_map[session]:
                homework_item_timers.append(self.create_hit(hi))

        return homework_item_timers

    def create_hit(self, hi):
        hit, exists = HomeworkItemTimer.objects.get_or_create(practice_id=self.id, homework_item_id=hi.id, defaults={'seconds': 0})

        return hit

    def __str__(self):
        return str(self.id)

class HomeworkItemTimer(models.Model):
    homework_item = models.ForeignKey(HomeworkItem, blank=False)
    practice = models.ForeignKey('Practice', blank=False)
    seconds = models.PositiveIntegerField()

    def __str__(self):
        return self.homework_item.__str__()

    def clock_time(self):
        return 'beep'
