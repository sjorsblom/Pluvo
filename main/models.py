from django.contrib.auth.models import AbstractUser
from django.db.models import CharField, DateField, EmailField, ForeignKey, DateTimeField, FloatField
from django.db.models import Model, CASCADE
from datetime import datetime


class User(AbstractUser):
    """ Extention on django user model """
    age = DateField(null=True)


class Score(Model):
    user = ForeignKey(User, on_delete=CASCADE)
    date = DateTimeField(default=datetime.now, blank=True)
    score = FloatField()
