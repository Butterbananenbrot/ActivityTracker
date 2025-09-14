import datetime

from django.test import TestCase
from django.utils import timezone

from .models import SleepInterval

class SleepIntervalModelTest(TestCase):
    """TestCase for the SleepInterval model validation methods."""

    def test_sleep_interval_is_shorter_than_20_hours(self):
        """Test that sleep_interval_is_shorter_than_20_hours() returns False for intervals longer than 20 hours."""
        overlong_sleep_interval = SleepInterval(start_time=timezone.now() - datetime.timedelta(hours=100),
                                                end_time=timezone.now() - datetime.timedelta(hours=1))
        self.assertIs(overlong_sleep_interval.sleep_interval_is_shorter_than_20_hours(), False)

    def test_end_time_after_start_time(self):
        """Test that end_time_after_start_time() returns False if end_time is before start_time."""
        impossible_sleep_interval = SleepInterval(start_time=timezone.now() - datetime.timedelta(hours=1),
                                                  end_time=timezone.now() - datetime.timedelta(hours=10))
        self.assertIs(impossible_sleep_interval.end_time_after_start_time(), False)
