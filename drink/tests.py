from django.test import TestCase
from .models import Drink

class DrinkModelTest(TestCase):
    """TestCase for the Drink model validation methods."""

    def test_max_one_liter(self):
        """Test that max_one_liter() returns False for drinks larger than 1000 milliliters."""
        unrealistically_large_drink = Drink(milliliters=1500)
        self.assertIs(unrealistically_large_drink.max_one_liter(), False)
