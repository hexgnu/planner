from django.core.management.base import BaseCommand
from planner import settings
import csv
import os

import random

from lessons.models import Lesson, HomeworkItem
from practices.models import HomeworkItemTimer, Practice

class Command(BaseCommand):
    args = '<foo bar ...>'
    help = 'our help string comes here'

    def handle(self, *args, **options):
        Lesson.objects.all().delete()
        HomeworkItem.objects.all().delete()
        HomeworkItemTimer.objects.all().delete()
        with open(os.path.join(settings.BASE_DIR,'lessons/management/commands/seeds.csv'), 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                lesson = Lesson.objects.create(scheduled_at=row['Date'], notes=row['Notes'])

                homework_items = ['Ornithology','Night and Day','Bach Invention No 2','Lush Life','Banacos Exercise #2','Banacos Exercise #3','Body and Soul','Anthropology','Banacos Exercise #4']

                for hi in homework_items:
                    if row[hi] != '':
                        hii, exists = HomeworkItem.objects.get_or_create(proficiency=row[hi], name=hi)
                        hii.lesson_set.add(lesson)


                minutes_of_practice = random.randint(15, 45)

                practice_sessions = random.randint(2,5)

                for i in range(practice_sessions):
                    print("Practice session {}".format(i))
                    practice, is_new = Practice.objects.get_or_create(finished=False, lesson=lesson)

                    plan = practice.plan()

                    avg_time = minutes_of_practice / len(plan)
                    
                    for hit in plan:
                        hit.seconds = avg_time * 60 * (0.7 + random.random()*0.3)
                        hit.save()

                    practice.finished = True
                    practice.save()

                print(row)
