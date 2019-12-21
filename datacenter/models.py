import pytz
import datetime
from django.db import models
from django.utils import timezone


class Passcard(models.Model):
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    passcode = models.CharField(max_length=200, unique=True)
    owner_name = models.CharField(max_length=255)

    def __str__(self):
        if self.is_active:
            return self.owner_name
        return f'{self.owner_name} (inactive)'


class Visit(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    passcard = models.ForeignKey(Passcard)
    entered_at = models.DateTimeField()
    leaved_at = models.DateTimeField(null=True)

    def __str__(self):
        return "{user} entered at {entered} {leaved}".format(
            user=self.passcard.owner_name,
            entered=self.entered_at,
            leaved= "leaved at " + str(self.leaved_at) if self.leaved_at else "not leaved"
        )

def get_duration(visit):
    if not visit.leaved_at:
        now = timezone.now()
        duration = (now - visit.entered_at).seconds
    else:
        duration = (visit.leaved_at - visit.entered_at).seconds
    return duration

def format_duration(duration):
    return f'{duration//3600}ч. {(duration%3600)//60}мин.'

def is_visit_long(duration):
    return duration > 3600



  