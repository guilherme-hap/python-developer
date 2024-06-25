from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.


class Event(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    event_date = models.DateTimeField(verbose_name='Date of Event')
    creation_date = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'event'

    def __str__(self):
        return self.title

    def get_event_date(self):
        return self.event_date.strftime('%d/%m/%Y %H:%Mhr')

    def get_event_input_date(self):
        return self.event_date.strftime('%Y-%m-%dT%H:%M')

    def get_delayed_event(self):
        if self.event_date < datetime.now():
            return True
        else:
            return False
