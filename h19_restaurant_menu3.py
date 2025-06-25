"""HARD - Restaurant menu"""

# Solution 3

class Dish:
    def __init__(self, name, preparation_time, dish_type):
        self.name = name
        self.preparation_time = preparation_time
        self.dish_type = dish_type
    
    def __eq__(self, other):
        return self.preparation_time == other.preparation_time

    def __gt__(self, other):
        return self.preparation_time > other.preparation_time

    def __ge__(self, other):
        return self.preparation_time >= other.preparation_time
    
    def __lt__(self, other):
        return not self.__gt__(other)

    def __le__(self, other):
        return not self.__ge__(other)


class Menu:
    def __init__(self, name, menu=None):
        self.name = name
        self.food = menu or {n: [] for n in ("starter", "dish", "dessert")}

    def __str__(self):
        menu = [[k.upper()] for k in self.food.keys()]
        for i, dish in enumerate(self.food.values()):
            menu[i].extend(d.name for d in sorted(dish, key=lambda d: d.preparation_time))
        return "\n\n".join("\n".join(dish) for dish in menu)

    def __add__(self, other):
        menu = {k: self.food[k] + other.food[k] for k in self.food.keys()}
        return Menu(f"{self.name} & {other.name}", menu)
      
    def add_dish(self, dish):
        self.food[dish.dish_type].append(dish)
    
    def get_starters(self):
        return self.food["starter"]
    
    def get_dishes(self):
        return self.food["dish"]
    
    def get_desserts(self):
        return self.food["dessert"]
    
    def get_minimum_preparation_time(self):
        return sum(min((d.preparation_time for d in dish), default=0) for dish in self.food.values())

    def get_maximum_preparation_time(self):
        return sum(max((d.preparation_time for d in dish), default=0) for dish in self.food.values())


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
