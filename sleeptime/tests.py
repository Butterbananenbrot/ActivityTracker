import datetime

from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from django.utils import timezone

from .models import SleepInterval

class DrinkModelTest(TestCase):
    def test_sleep_interval_is_shorter_than_20_hours(self):
        """
        Prüfen der Start- und Endzeiten: immer maximal 20 Stunden Schlaf nur?
        sleep_interval_is_shorter_than_20_hours() gibt False zurück für Schlafintervalle, die länger als 20 Stunden sind.
        """
        overlong_sleep_interval = SleepInterval(start_time=timezone.now() - datetime.timedelta(hours=100),
                               end_time=timezone.now() - datetime.timedelta(hours=1))
        self.assertIs(overlong_sleep_interval.sleep_interval_is_shorter_than_20_hours(), False)
    def test_end_time_after_start_time(self):
        """
        Prüft, ob ein Schlafintervall, welcher vor einer Stunde angefangen hat und vor zehn Stunden geendet hat
        wie vorgesehen als Falsch erkannt wird
        """
        impossible_sleep_interval = SleepInterval(start_time=timezone.now() - datetime.timedelta(hours=1),
                                       end_time=timezone.now() - datetime.timedelta(hours=10))
        self.assertIs(impossible_sleep_interval.end_time_after_start_time(), False)
