from django.shortcuts import render
from django.http import HttpResponse
from .models import Lesson, HomeworkItem
from practices.models import Practice,HomeworkItemTimer
import random
import django
import datetime
import pandas as pd
import matplotlib.pyplot as plt

from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
from matplotlib.dates import DateFormatter


def index(request):
    last_10_lessons = Lesson.objects.order_by('-scheduled_at')[:10]
    items = last_10_lessons.first().homework_items.all()
    return render(request, 'lessons/index.html', {'lessons': last_10_lessons, 'homework_items': items})

# Lesson is edited by teacher
def teacher_edit(request):
    return render(request, 'teacher_edit.html', {'lesson': Lesson})
    
# Lesson is edited by student
def student_edit(request):
    return render(request, 'student_edit.html', {'lesson': Lesson})

def practice_png(request):
    lessons = Lesson.objects.order_by('-scheduled_at').all()

    rows = []
    
    for l in lessons:
        for hi in l.homework_items.all():
            if 'homework_item_name' not in request.GET.keys() or hi.name == request.GET['homework_item_name']:
                practices = Practice.objects.filter(lesson_id = l.id)
                timers = HomeworkItemTimer.objects.filter(practice__in=practices, homework_item_id=hi.id)
                total_seconds = sum([t.seconds for t in timers])
                rows.append({'date': l.scheduled_at, 'item': hi.name, 'y': total_seconds})

    df = pd.DataFrame(rows)

    df = df.pivot_table(index=['date'], columns='item')
    df.columns = df.columns.droplevel().rename(None)


    fig = Figure()
    ax = fig.add_subplot(111)
    df.plot(ax=ax)
    canvas = FigureCanvas(fig)
    response = HttpResponse(content_type='image/png')
    canvas.print_png(response)
    return response

def proficiency_png(request):
    lessons = Lesson.objects.order_by('-scheduled_at').all()

    rows = []
    
    for l in lessons:
        for hi in l.homework_items.all():
            if 'homework_item_name' not in request.GET.keys() or hi.name == request.GET['homework_item_name']:
                practices = Practice.objects.filter(lesson_id = l.id)
                timers = HomeworkItemTimer.objects.filter(practice__in=practices, homework_item_id=hi.id)
                total_seconds = sum([t.seconds for t in timers])
                rows.append({'date': l.scheduled_at, 'item': hi.name, 'y': hi.proficiency})

    df = pd.DataFrame(rows)

    df = df.pivot_table(index=['date'], columns='item')
    df.columns = df.columns.droplevel().rename(None)


    fig = Figure()
    ax = fig.add_subplot(111)
    df.plot(drawstyle='steps', ax=ax).legend(bbox_to_anchor=(0.25, 0.4))

    canvas = FigureCanvas(fig)
    response = HttpResponse(content_type='image/png')
    canvas.print_png(response)
    return response



# Create your views here.
