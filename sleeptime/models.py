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
    sleeping_place = models.CharField(max_length=1, choices=SLEEPING_PLACE_CHOICES)
    recreation = models.IntegerField(choices=ONE_TO_TEN_SCALE)
    tiredness_before_sleeping = models.IntegerField(choices=ONE_TO_TEN_SCALE)

    def __str__(self):
        # Da wir die Methode auf einem Objekt aufrufen,
        # müssen wir SLEEPING_PLACE_CHOICES_MAP als Klassenattribut abrufen
        return SleepInterval.SLEEPING_PLACE_CHOICES_MAP.get(self.sleeping_place)
