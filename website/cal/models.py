from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django import forms
from datetime import datetime
from phone_field import PhoneField


class Event(models.Model):
    title = models.TextField(u'Name of the Meeting', help_text=u'name of the Meeting', blank=False, null=False)
    meetid = models.TextField(u'Meeting ID', help_text=u'meeting id', blank=False, null=False, default='1')
    participant = models.ForeignKey(User, on_delete=models.CASCADE, default='1')
    #day = models.DateField(u'Day of the event', help_text=u'Day of the event', default=datetime.now)
    start_time = models.DateTimeField(u'Starting time', help_text=u'Starting time')
    end_time = models.DateTimeField(u'Final time', help_text=u'Final time')
    materials = models.FileField(upload_to='documents/', blank=True)
   
    @property
    def get_html_url(self):
        url = reverse('event_edit', args=(self.id,))
        return f'<a href="{url}"> {self.title} </a>'
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('calendar')

