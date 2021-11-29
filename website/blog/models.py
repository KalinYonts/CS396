from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django import forms
from datetime import datetime
from phone_field import PhoneField

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    file = models.FileField(upload_to='documents/', blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})


class Category(models.Model):
    name = models.CharField(max_length = 50, null = True, blank = True)

    def __str__(self):
        return self.name

class Product(models.Model):
    category_name = models.ForeignKey(Category, on_delete = models.CASCADE,null = True, blank = True)
    item_name = models.CharField(max_length = 50, null = True, blank = True)
    total_quantity = models.IntegerField(default = 0, null = True, blank = True)
    issued_quantity = models.IntegerField(default = 0, null = True, blank = True)
    received_quantity = models.IntegerField(default = 0, null = True, blank = True)
    unit_price = models.IntegerField(default = 0, null = True, blank = True)

    def __str__(self):
        return self.item_name
    

class Sale(models.Model):
    item = models.ForeignKey(Product, on_delete = models.CASCADE)
    quantity = models.IntegerField(default = 0, null = True, blank = True)
    amount_received = models.IntegerField(default = 0, null = True, blank = True)
    issued_to = models.CharField(max_length = 50, null = True, blank = True)
    unit_price = models.IntegerField(default = 0, null = True, blank = True)

    def get_total(self):
        total = self.quantity * self.item.unit_price
        return int(total)

    def get_change(self):
        change = self.get_total() - self.amount_received
        return abs(int(change))

    def __str__(self):
        return self.item.item_name

DOCTOR_NAMES = (
    ('Smith', 'SMITH'),
    ('Williams', 'WILLIAMS'),
    ('Kumal', 'KUMAL'),
    ('Price', 'PRICE'),
    ('Edwards', 'EDWARDS'),
    ('Other', 'OTHER')
    )
class Doctor(models.Model):
    name = models.CharField(max_length = 10, choices=DOCTOR_NAMES, default='other')
    def __str__(self):
        return self.name

class Health(models.Model):
    doctor_name = models.ForeignKey(Doctor, on_delete = models.CASCADE,null = True, blank = True)
    phone = PhoneField(blank=True, help_text='phone number')
    email = models.EmailField(max_length=70, blank=True, unique=True)
    prescriptions = models.CharField(max_length = 50, null = True, blank = True)
    dose = models.IntegerField(default = 0, null = True, blank = True)
    dosetime = models.TimeField(u'Dose time', help_text=u'Dose time')
    def __str__(self):
        return self.prescriptions









