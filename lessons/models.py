from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class Lesson(models.Model):
    scheduled_at    = models.DateTimeField()
    created_at      = models.DateTimeField(auto_now_add=True)
    updated_at      = models.DateTimeField(auto_now=True)
    notes           = models.TextField()

    # has many attachments
    # has many teachers and students
    # has many 

class Attachment(models.Model):
    url             = models.URLField()

class HomeworkItem(models.Model):
    name            = models.CharField(max_length=255, unique=True, blank=False)
    proficiency     = models.IntegerField(default=1, validators=[MaxValueValidator(5), MinValueValidator(1)])
