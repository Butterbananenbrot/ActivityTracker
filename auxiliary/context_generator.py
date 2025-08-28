from drink.models import Drink


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