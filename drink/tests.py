from django.test import TestCase
from .models import Drink

class DrinkModelTest(TestCase):
    def test_max_one_liter(self):
        # prüft die Validierungsmethode, erwartete Ausgabe ist False
        unrealistically_large_drink = Drink(milliliters=1500)
        self.assertIs(unrealistically_large_drink.max_one_liter(), False)
