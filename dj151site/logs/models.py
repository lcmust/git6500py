from django.db import models
from django.forms import ModelForm
import datetime

class Ipaddres(models.Model):
    ip_addre = models.IPAddressField()

