from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from auxiliary.choices import ONE_TO_TEN_SCALE

class Drink(models.Model):
    # Klassenattribut
    DRINK_CHOICES = [(choice, choice) for choice in ["Water", "Coffee", "Beer"]]

    drink = models.CharField(max_length=20, choices=DRINK_CHOICES, default=DRINK_CHOICES[0][0])
    #thirst_quenched = models.IntegerChoices("Thirst Quenched", "1 2 3 4 5 6 7 8 9 10")
    thirst_quenched = models.IntegerField(choices=ONE_TO_TEN_SCALE, default=1) # import from aux module
    milliliters = models.IntegerField(validators=[MinValueValidator(20), MaxValueValidator(1000)])

    def __str__(self):
        return f"{self.drink}, ({self.milliliters} ml)"

    def max_one_liter(self ):
        # Validierungsmethode: TRUE bei korrektem Input
        check = self.milliliters <= 1000
        return check
