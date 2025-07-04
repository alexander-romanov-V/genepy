"""Decorators guide"""

# Декоратор - паттерн програмиирования, который позволяет добавлять
# новый функционал к нашей функции, не видоизменяя саму функцию

# Примеры:
# 1. Подсчет времени выполнения функции
# 2. Логирование параметров функции
# 3. Повтор функции в случае ошибки
# 4. Ограничение на частый вызов функции

# Стандартное применение декоратора (синтаксический сахар])
# @deco(deco_params)
# def my_func(func_params):
#     return 124

# Эквивалентное применение декоратора (переопределение функции и вызов декоратора и передача ему этой функции, как параметра)
# my_func = deco(deco_params)(my_func)(func_params)


# ----------------------------------------------------------------------------
# Скелет декоратора
from typing import Callable
from functools import wraps


def empty_deco(func: Callable):
    @wraps(func)  # сохряняет докстринг, имя функции и пр.
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        return res
    return wrapper


# ----------------------------------------------------------------------------
# Скелет декоратора с параметром
def param_calls(param):
    def wrapper(func: Callable):
        @wraps(func)
        def inner_wrapper(*args, **kwargs):
            nonlocal param
            res = func(*args, **kwargs)
            return res
        return inner_wrapper

    return wrapper


