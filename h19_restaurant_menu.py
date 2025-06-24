"""HARD - Restaurant menu"""

# Solution 1 - my first
DishType = ["starter", "dish", "dessert"]


class Dish:
    """Dish in restaurant"""

    def __init__(self, name: str, preparation_time: int, dish_type: str) -> None:
        self.name = name
        if dish_type not in DishType:
            raise ValueError("dish_type can be only: " + ", ".join(DishType))
        self.preparation_time = preparation_time
        self.dish_type = dish_type

    def __eq__(self, other) -> bool:
        return self.preparation_time == other.preparation_time

    def __ne__(self, other) -> bool:
        return self.preparation_time != other.preparation_time

    def __lt__(self, other) -> bool:
        return self.preparation_time < other.preparation_time

    def __gt__(self, other) -> bool:
        return self.preparation_time > other.preparation_time

    def __le__(self, other) -> bool:
        return self.preparation_time <= other.preparation_time

    def __ge__(self, other) -> bool:
        return self.preparation_time >= other.preparation_time


class Menu:
    """Menu of Dishes in restaurant"""

    def __init__(self, name: str) -> None:
        self.name = name
        self.dishes = []

    def add_dish(self, dish: Dish) -> None:
        """Add dish to the Menu"""
        self.dishes.append(dish)

    def get_starters(self) -> list[Dish]:
        """Returns only starters from menu"""
        return [d for d in self.dishes if d.dish_type == "starter"]

    def get_dishes(self) -> list[Dish]:
        """Returns only dishes from menu"""
        return [d for d in self.dishes if d.dish_type == "dish"]

    def get_desserts(self) -> list[Dish]:
        """Returns only desserts from menu"""
        return [d for d in self.dishes if d.dish_type == "dessert"]

    def get_minimum_preparation_time(self) -> int:
        """Returns sum of minimum of preparation times of starters, dishes, and desserts"""
        return (
            min([d.preparation_time for d in self.get_starters()], default=0)
            + min([d.preparation_time for d in self.get_dishes()], default=0)
            + min([d.preparation_time for d in self.get_desserts()], default=0)
        )

    def get_maximum_preparation_time(self) -> int:
        """Returns sum of maximum of preparation times of starters, dishes, and desserts"""
        return (
            max([d.preparation_time for d in self.get_starters()], default=0)
            + max([d.preparation_time for d in self.get_dishes()], default=0)
            + max([d.preparation_time for d in self.get_desserts()], default=0)
        )

    def __add__(self, other):
        menu = Menu(self.name + " & " + other.name)
        menu.dishes = self.dishes.copy() + other.dishes.copy()
        return menu

    def __str__(self) -> str:
        return (
            "STARTER\n"
            + "\n".join(d.name for d in self.get_starters())
            + "\n\nDISH\n"
            + "\n".join(d.name for d in self.get_dishes())
            + "\n\nDESSERT\n"
            + "\n".join(d.name for d in self.get_desserts())
        )


if __name__ == "__main__":
    menu_1 = Menu("One")
    menu_1.add_dish(Dish("eggs & mayonaise", 5, "starter"))
    menu_1.add_dish(Dish("burger", 15, "dish"))
    menu_1.add_dish(Dish("waffle", 20, "dessert"))

    menu_2 = Menu("Two")
    menu_2.add_dish(Dish("salad", 10, "starter"))
    menu_2.add_dish(Dish("pizza", 20, "dish"))
    menu_2.add_dish(Dish("chocolate cookie", 30, "dessert"))

    menu_3 = menu_1 + menu_2

    print(menu_3.name)

    print(menu_3)
