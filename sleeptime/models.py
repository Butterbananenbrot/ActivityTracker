import datetime

from django.db import models
from auxiliary.choices import ONE_TO_TEN_SCALE

class SleepInterval(models.Model):
    """Model representing a sleep interval."""

    SLEEPING_PLACE_CHOICES = [(choice, choice) for choice in ["Bed", "Sofa", "Floor"]]

    start_time = models.DateTimeField()
    """Time when the sleep interval started."""

    end_time = models.DateTimeField()
    """Time when the sleep interval ended."""

    sleeping_place = models.CharField(max_length=20, choices=SLEEPING_PLACE_CHOICES, default=SLEEPING_PLACE_CHOICES[0][0])
    """Place where the user slept (e.g. Bed, Sofa, Floor)."""

    recreation = models.IntegerField(choices=ONE_TO_TEN_SCALE, default=1)
    """Recreation value after sleeping (1-10)."""

    tiredness_before_sleeping = models.IntegerField(choices=ONE_TO_TEN_SCALE, default=1)
    """Tiredness value before sleeping (1-10)."""

    def __str__(self):
        """String representation of the sleep interval."""
        return f"Sleeping at {self.sleeping_place} lasting {self.end_time - self.start_time} with id {self.id}"

    def sleep_interval_is_shorter_than_20_hours(self):
        """Returns True if the sleep interval is shorter than 20 hours."""
        check = self.end_time - self.start_time < datetime.timedelta(hours=20)
        return check

    def end_time_after_start_time(self):
        """Returns True if the end time is after the start time."""
        return self.end_time > self.start_time