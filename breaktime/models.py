from django.db import models
import datetime
from auxiliary.choices import ONE_TO_TEN_SCALE

class Break(models.Model):
    ACTIVITY_CHOICES = [
        ("WA", "Walk"),
        ("SL", "Sleep"),
        ("EA", "Eat"),
        ("SM", "Smalltalk"),
    ]
    PLACE_CHOICES = [
        ("O", "Office"),
        ("P", "Park"),
        ("F", "Forest"),
        ("C", "Cafe"),
    ]
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    activity = models.CharField(max_length=2, choices=ACTIVITY_CHOICES, default="WA")
    # activity = models.CharField("Activity", choices=["Walk", "Sleep", "Eat", "Smalltalk"], default="Smalltalk")
    place = models.CharField(max_length=1, choices=PLACE_CHOICES, default="P")
    recreation = models.IntegerField(choices=ONE_TO_TEN_SCALE, default=5) # import from aux module

    def __str__(self):
        return self.activity

    def break_took_max_eight_hours(self ):
        # Validierungsmethode: TRUE bei korrektem Input
        check = self.end_time - self.start_time < datetime.timedelta(hours=8)
        return check

    def end_time_after_start_time(self):
        # Validierungsmethode: TRUE bei korrektem Input
        return self.end_time > self.start_time

    def rec_value_between_one_and_ten(self):
        # Validierungsmethode für import der Scale aus choices.py: TRUE bei korrektem Input
        return 1 <= self.recreation <= 10
