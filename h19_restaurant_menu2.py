"""HARD - Restaurant menu"""

# Solution 2

from dataclasses import dataclass, field

KINDS = "starter", "dish", "dessert"


@dataclass(order=True)
class Dish:
    name: str = field(compare=False)
    preparation_time: float
    dish_type: str = field(compare=False)

    def __str__(self):
        return self.name


@dataclass
class Menu:
    name: str
    dishes: list[str] = field(default_factory=list)

    def add_dish(self, dish):
        self.dishes.append(dish)

    def _get(self, type):
        return sorted([dish for dish in self.dishes if dish.dish_type == type])

    def get_starters(self):
        return self._get("starter")

    def get_dishes(self):
        return self._get("dish")

    def get_desserts(self):
        return self._get("dessert")

    def get_minimum_preparation_time(self):
        return sum(
            min([dish.preparation_time for dish in self._get(kind)], default=0)
            for kind in KINDS
        )

    def get_maximum_preparation_time(self):
        return sum(
            max([dish.preparation_time for dish in self._get(kind)], default=0)
            for kind in KINDS
        )

    def __str__(self):
        return "\n\n".join(
            dish_type.upper()
            + "\n"
            + "\n".join(dish.name for dish in self._get(dish_type))
            for dish_type in KINDS
        )

    def __add__(self, other):
        if not isinstance(other, Menu):
            return NotImplemented
        return Menu(self.name + " & " + other.name, self.dishes + other.dishes)


if __name__ == "__main__":
    menu_1 = Menu("One")
    menu_1.add_dish(Dish("eggs & mayonaise", 5, "starter"))
    menu_1.add_dish(Dish("burger", 15, "dish"))
    menu_1.add_dish(Dish("waffle", 30, "dessert"))

    menu_2 = Menu("Two")
    menu_2.add_dish(Dish("salad", 10, "starter"))
    menu_2.add_dish(Dish("pizza", 20, "dish"))
    menu_2.add_dish(Dish("chocolate cookie", 20, "dessert"))

    menu_3 = menu_1 + menu_2

    print(menu_3.name)

    print(menu_3)
