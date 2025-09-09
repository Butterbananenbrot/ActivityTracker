from django.db import models
import datetime
from auxiliary.choices import ONE_TO_TEN_SCALE

class Break(models.Model):


    ACTIVITY_CHOICES = [(choice, choice) for choice in ["Walk", "Sleep", "Eat", "Smalltalk"]]
    PLACE_CHOICES = [(choice, choice) for choice in ["Office", "Park", "Forest", "Cafe"]]

    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    activity = models.CharField(max_length=20, choices=ACTIVITY_CHOICES, default=ACTIVITY_CHOICES[0][0])
    # activity = models.CharField("Activity", choices=["Walk", "Sleep", "Eat", "Smalltalk"], default="Smalltalk")
    place = models.CharField(max_length=20, choices=PLACE_CHOICES, default=PLACE_CHOICES[0][0])
    recreation = models.IntegerField(choices=ONE_TO_TEN_SCALE, default=5) # import from aux module

    def __str__(self):
        return f"{self.activity} at {self.place} lasting {self.end_time - self.start_time} with id {self.id}"

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
