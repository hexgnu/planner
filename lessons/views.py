from django.shortcuts import render
from django.http import HttpResponse
from .models import Lesson, HomeworkItem

def index(request):
    last_10_lessons = Lesson.objects.order_by('-scheduled_at')[:10]
    items = HomeworkItem.objects.all()
    return render(request, 'lessons/index.html', {'lessons': last_10_lessons, 'homework_items': items})

# Lesson is edited by teacher
def teacher_edit(request):
    return render(request, 'teacher_edit.html', {'lesson': Lesson})
    
# Lesson is edited by student
def student_edit(request):
    return render(request, 'student_edit.html', {'lesson': Lesson})


# Create your views here.
