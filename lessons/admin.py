from django.contrib import admin

# Register your models here.
from .models import Lesson, Attachment, HomeworkItem

admin.site.register(Lesson)
admin.site.register(Attachment)
admin.site.register(HomeworkItem)

