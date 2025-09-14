from django.db import models
import datetime
from auxiliary.choices import ONE_TO_TEN_SCALE


class Break(models.Model):
    """Model for break times taken by the user."""

    ACTIVITY_CHOICES = [(choice, choice) for choice in ["Walk", "Sleep", "Eat", "Smalltalk"]]
    PLACE_CHOICES = [(choice, choice) for choice in ["Office", "Park", "Forest", "Cafe"]]

    start_time = models.DateTimeField()
    """Time when the break started."""

    end_time = models.DateTimeField()
    """Time when the break ended."""

    activity = models.CharField(max_length=20, choices=ACTIVITY_CHOICES, default=ACTIVITY_CHOICES[0][0])
    """Type of activity during the break (e.g. Walk, Sleep, Eat, Smalltalk)."""

    place = models.CharField(max_length=20, choices=PLACE_CHOICES, default=PLACE_CHOICES[0][0])
    """Place where the break took place (e.g. Office, Park, Forest, Cafe)."""

    recreation = models.IntegerField(choices=ONE_TO_TEN_SCALE, default=5)
    """Recreation value of the break on a scale from 1 to 10."""

    def __str__(self):
        return f"{self.activity} at {self.place} lasting {self.end_time - self.start_time} with id {self.id}"

    def break_took_max_eight_hours(self):
        # Validierungsmethode: TRUE bei korrektem Input
        check = self.end_time - self.start_time < datetime.timedelta(hours=8)
        return check

    def end_time_after_start_time(self):
        # Validierungsmethode: TRUE bei korrektem Input
        return self.end_time > self.start_time

    def rec_value_between_one_and_ten(self):
        # Validierungsmethode für import der Scale aus choices.py: TRUE bei korrektem Input
        return 1 <= self.recreation <= 10
