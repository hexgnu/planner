from django.shortcuts import render

from lessons.models import Lesson

from .models import Practice

def index(request):
    practice = Practice.objects.get_or_create(finished=False)

    last_lesson = Lesson.objects.order_by('-scheduled_at').first()
    return render(request, 'practices/index.html', {'homework_items': last_lesson.homework_items.all(), 'lesson': last_lesson})
