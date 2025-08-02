from django.db import models

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
    RECREATION_CHOICES = models.IntegerChoices("Recreation", "1 2 3 4 5 6 7 8 9 10")
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    activity = models.CharField(max_length=2, choices=ACTIVITY_CHOICES)
    place = models.CharField(max_length=1, choices=PLACE_CHOICES)
    recreation = models.IntegerField(choices=RECREATION_CHOICES)
    def __str__(self):
        return self.activity
