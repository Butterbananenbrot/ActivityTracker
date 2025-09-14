import datetime

from django.test import TestCase
from django.utils import timezone

from .models import Break


class BreakModelTests(TestCase):
    """TestCase for the Break model validation methods."""

    def test_break_took_max_eight_hours(self):
        """Test that break_took_max_eight_hours() returns False for breaks longer than eight hours."""
        overlong_break = Break(start_time=timezone.now() - datetime.timedelta(hours=10),
                               end_time=timezone.now() - datetime.timedelta(hours=1))
        self.assertIs(overlong_break.break_took_max_eight_hours(), False)

    def test_end_time_after_start_time(self):
        """Test that end_time_after_start_time() returns False if end_time is before start_time."""
        impossible_times_break = Break(start_time=timezone.now() - datetime.timedelta(hours=1),
                                       end_time=timezone.now() - datetime.timedelta(hours=10))
        self.assertIs(impossible_times_break.end_time_after_start_time(), False)

    def test_rec_value_between_one_and_ten(self):
        """Test that rec_value_between_one_and_ten() returns False if recreation is out of bounds."""
        outside_bounds_recreation = Break(start_time=timezone.now()- datetime.timedelta(hours=1),
                                          end_time=timezone.now(), recreation=11)
        self.assertIs(outside_bounds_recreation.rec_value_between_one_and_ten(), False)
