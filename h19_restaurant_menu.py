"""HARD - Restaurant menu"""

# Solution 1 - my first
from enum import Enum, unique


@unique
class DishType(Enum):
    starter = 1
    dish = 2
    dessert = 3


class Dish:
    def __init__(self, name: str, preparation_time: int, dish_type: DishType) -> None:
        self.name = name
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
    def __init__(self, name: str) -> None:
        self.name = name
        self.dishes = []

    def add_dish(self, dish: Dish) -> None:
        self.dishes.append(dish)

    def get_starters(self) -> list[Dish]:
        return [d for d in self.dishes if d.dish_type == DishType.starter]

    def get_dishes(self) -> list[Dish]:
        return [d for d in self.dishes if d.dish_type == DishType.dish]

    def get_desserts(self) -> list[Dish]:
        return [d for d in self.dishes if d.dish_type == DishType.dessert]

    def get_minimum_preparation_time(self):
        starters_time = min(self.get_starters())
        dishes_time = min(self.get_dishes())
        desserts_time = min(self.get_desserts())
        return starters_time.preparation_time + dishes_time.preparation_time + desserts_time.preparation_time

    def get_maximum_preparation_time(self):
        starters_time = max(self.get_starters())
        dishes_time = max(self.get_dishes())
        desserts_time = max(self.get_desserts())
        return starters_time.preparation_time + dishes_time.preparation_time + desserts_time.preparation_time

    def __add__(self, other):
        menu = Menu(self.name + " & " + other.name)
        menu.dishes = self.dishes.copy() + other.dishes.copy()
        return menu
    

if __name__ == "__main__":
    menu_1 = Menu("One")
    menu_2 = Menu("Two")
    menu_3 = menu_1 + menu_2
    print(menu_3.name)
