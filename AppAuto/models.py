from django.db import models
from djmoney.models.fields import MoneyField
#from django.core.urlresolvers import reverse

# Create your models here.

class Vehicle(models.Model):
    name = models.CharField(max_length=45)
    model = models.CharField(max_length=54)
    price = MoneyField(max_digits=10, decimal_places=2, default_currency='USD')
    mileage = models.PositiveIntegerField(default=0)
    snapshot = models.ImageField(upload_to='media/')

    def __str__(self):
        return self.name

#  def get_absolute_url(self):
#       return reverse('index')

class ContactModel(models.Model):
    name = models.CharField(max_length=45)
    email = models.EmailField()
    text = models.TextField()


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('index')

