import uuid
import datetime

from django.db import models
from paranoid_model.models import Paranoid


def year_choices():
    return [(r, r) for r in range(1960, datetime.date.today().year+1)]


def current_year():
    return datetime.date.today().year


class Car(Paranoid):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.TextField()
    make = models.TextField()
    model = models.TextField()
    year = models.IntegerField(choices=year_choices(), default=current_year)

    def __str__(self):
        return self.name


class Service(Paranoid):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    service = models.TextField()
    cost = models.IntegerField(default=0)

    def __str__(self):
        return self.service
