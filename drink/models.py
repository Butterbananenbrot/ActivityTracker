from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from auxiliary.choices import ONE_TO_TEN_SCALE


class Drink(models.Model):
    """Model representing a drink event."""

    DRINK_CHOICES = [(choice, choice) for choice in ["Water", "Coffee", "Beer"]]

    drink = models.CharField(max_length=20, choices=DRINK_CHOICES, default=DRINK_CHOICES[0][0])
    """Type of drink (e.g. Water, Coffee, Beer)."""

    thirst_quenched = models.IntegerField(choices=ONE_TO_TEN_SCALE, default=1)
    """How much the drink quenched thirst (1-10)."""

    milliliters = models.IntegerField(validators=[MinValueValidator(20), MaxValueValidator(1000)])
    """Amount of drink in milliliters (20-1000)."""

    def __str__(self):
        """String representation of the drink event."""
        return f"{self.milliliters} ml {self.drink} quenching {self.thirst_quenched} thirst"

    def max_one_liter(self):
        """Returns True if the drink is at most 1000 milliliters."""
        check = self.milliliters <= 1000
        return check
