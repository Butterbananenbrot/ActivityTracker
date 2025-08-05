import datetime

from django.db import models
from auxiliary.choices import ONE_TO_TEN_SCALE

class SleepInterval(models.Model):
    # Klassenattribut
    SLEEPING_PLACE_CHOICES = [
        ("B", "Bed"),
        ("S", "Sofa"),
        ("F", "Floor"), # Damit eine dritte Wahl vorhanden ist
    ]


    # Umwandeln in ein Dictionary, damit in __str__ nutzbar
    SLEEPING_PLACE_CHOICES_MAP = dict(SLEEPING_PLACE_CHOICES) # Klassenattribut
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    sleeping_place = models.CharField(max_length=1, choices=SLEEPING_PLACE_CHOICES, default="B")
    recreation = models.IntegerField(choices=ONE_TO_TEN_SCALE, default=1)
    tiredness_before_sleeping = models.IntegerField(choices=ONE_TO_TEN_SCALE, default=1)

    def __str__(self):
        # Da wir die Methode auf einem Objekt aufrufen,
        # müssen wir SLEEPING_PLACE_CHOICES_MAP als Klassenattribut abrufen
        return SleepInterval.SLEEPING_PLACE_CHOICES_MAP.get(self.sleeping_place)

    def sleep_interval_is_shorter_than_20_hours(self):
        # Validierungsmethode: TRUE bei korrektem Input
        check = self.end_time - self.start_time < datetime.timedelta(hours=20)
        return check

    def end_time_after_start_time(self):
        # Validierungsmethode: TRUE bei korrektem Input
        return self.end_time > self.start_time