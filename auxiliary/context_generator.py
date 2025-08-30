from drink.models import Drink
from breaktime.models import Break
from sleeptime.models import SleepInterval


def create_drink_data_context():
    mapping = {"W": "Water", "C": "Coffee", "B": "Beer"}
    drinks = [
        {
            "drink_label": mapping.get(d.drink, d.drink),
            "thirst_quenched": d.thirst_quenched,
            "milliliters": d.milliliters,
        }
        for d in Drink.objects.all()
    ]
    return drinks


def create_break_data_context():
    breaks = [
        {
            "start_time": b.start_time,
            "end_time": b.end_time,
            "activity": b.activity,
            "place": b.place,
            "recreation": b.recreation
        }
        for b in Break.objects.all()
    ]
    return breaks


def create_sleepinterval_data_context():
    sleepintervals = [
        {
            "start_time": s.start_time,
            "end_time": s.end_time,
            "sleeping_place": s.sleeping_place,
            "recreation": s.recreation,
            "tiredness_before_sleeping": s.tiredness_before_sleeping
        }
        for s in SleepInterval.objects.all()
    ]
    return sleepintervals
