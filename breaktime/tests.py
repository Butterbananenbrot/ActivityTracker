import datetime

from django.test import TestCase
from django.utils import timezone

from .models import Break


class BreakModelTests(TestCase):
    def test_break_took_max_eight_hours(self):
        """
        Prüfen der Start- und Endzeiten: immer maximal 8 Stunden Pause?
        break_took_max_eight_hours() returns False for questions whose length is more than eight hours.
        """
        overlong_break = Break(start_time=timezone.now() - datetime.timedelta(hours=10),
                               end_time=timezone.now() - datetime.timedelta(hours=1))
        self.assertIs(overlong_break.break_took_max_eight_hours(), False)

    def test_end_time_after_start_time(self):
        """
        Prüft, ob eine Pause die vor 1 Stunde angefangen und vor 10 Stunden geendet hat
        wie vorgesehen als Falsch erkannt wird
        """
        impossible_times_break = Break(start_time=timezone.now() - datetime.timedelta(hours=1),
                                       end_time=timezone.now() - datetime.timedelta(hours=10))
        self.assertIs(impossible_times_break.end_time_after_start_time(), False)

    def test_rec_value_between_one_and_ten(self):
        """
        Prüft, ob die Recreation wie vorgesehen zwischen eins und zehn ist
        :return: TRUE wenn Test bestanden
        """
        outside_bounds_recreation = Break(start_time=timezone.now()- datetime.timedelta(hours=1),
                                          end_time=timezone.now(), recreation=11)
        self.assertIs(outside_bounds_recreation.rec_value_between_one_and_ten(), False)
