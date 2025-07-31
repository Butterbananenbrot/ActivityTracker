from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Drink(models.Model):
    # Klassenattribut
    DRINK_CHOICES = [
        ("W", "Water"),
        ("C", "Coffee"),
        ("B", "Beer"),
    ]
    # Umwandeln in ein Dictionary, damit in __str__ nutzbar
    DRINK_CHOICES_MAP = dict(DRINK_CHOICES)  # Klassenattribut

    drink = models.CharField(max_length=1, choices=DRINK_CHOICES)
    thirst_quenched = models.IntegerChoices("Thirst Quenched", "1 2 3 4 5 6 7 8 9 10")
    milliliters = models.IntegerField(validators=[MinValueValidator(20), MaxValueValidator(1000)])

    def __str__(self):
        return Drink.DRINK_CHOICES_MAP.get(self.drink)
