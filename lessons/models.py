from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class Lesson(models.Model):
    scheduled_at    = models.DateTimeField()
    created_at      = models.DateTimeField(auto_now_add=True)
    updated_at      = models.DateTimeField(auto_now=True)
    notes           = models.TextField()
    attachments     = models.ManyToManyField('Attachment', blank=True)
    homework_items  = models.ManyToManyField('HomeworkItem', blank=True)

    # has many attachments
    # has many teachers and students
    # has many 

    def __str__(self):
        return self.scheduled_at.strftime('%D')

class Attachment(models.Model):
    url             = models.URLField()
    lessons         = models.ManyToManyField(Lesson, blank=False, through=Lesson.attachments.through)

class HomeworkItem(models.Model):
    name            = models.CharField(max_length=255, blank=False)
    proficiency     = models.IntegerField(default=1, validators=[MaxValueValidator(5), MinValueValidator(1)])
    lessons         = models.ManyToManyField(Lesson, blank=False, through=Lesson.homework_items.through)

    class Meta:
        unique_together = ('name', 'proficiency',)

    def __str__(self):
        return "{} ({}/5)".format(self.name, self.proficiency)
