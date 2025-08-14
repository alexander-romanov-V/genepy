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


# ----------------------------------------------------------------------------
# # Скелет декоратора для асинхронной функции ( v.3.5 ?)
# from typing import Coroutine
# import asyncio

# def async_deco(coroutine: Coroutine):
#     async def wrapper(*args, **kwargs):
#         res = await coroutine(*args, **kwargs)
#         return res
#     return wrapper


# @async_deco
# async def my_async_func():
#     await asyncio.sleep(0.5)
#     return 1

# await my_async_func()
# # asyncio.run()


# ----------------------------------------------------------------------------
# ----------------------------------------------------------------------------
import time


def timer_deco(func: Callable):
    """1. Подсчет времени выполнения функции"""

    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        res = func(*args, **kwargs)
        end = time.time()
        print(f"Исполнение {func.__name__} заняло {end-start:.3} сек.")
        return res

    return wrapper


@timer_deco
def my_func2(sleep_time: int):
    time.sleep(sleep_time)
    return 1350


# print(my_func2(1))


# ----------------------------------------------------------------------------
def limit_calls(limit: int):
    """4. Ограничение на частый вызов функции"""

    def wrapper(func: Callable):
        @wraps(func)
        def inner_wrapper(*args, **kwargs):
            nonlocal limit
            if limit <= 0:
                print(f"Нельзя вызвать функцию {func.__name__}")
                return
            res = func(*args, **kwargs)
            limit -= 1
            return res

        return inner_wrapper

    return wrapper


@limit_calls(2)
def my_func3(sleep_time: int):
    """Поспать немного"""
    time.sleep(sleep_time)
    return 135


# my_func3 = limit_calls(2)(my_func3)

# print(my_func3(1))
# print(my_func3(1))

# print(my_func3(1))

# print(my_func3.__name__)
# print(my_func3.__doc__)


# ----------------------------------------------------------------------------
# Кэширование вызовов
from functools import lru_cache


@lru_cache(maxsize=5)
def my_long_calc():
    time.sleep(3)
    return 42


# print(my_long_calc())
# print(my_long_calc())
# print(my_long_calc())

# ----------------------------------------------------------------------------
# Контекстный менеджер синхронный (with)
from contextlib import contextmanager


@contextmanager
def ctx_manager():
    print("Hello")
    yield
    print("end")


# with ctx_manager() as man:
#     print("123")


# ----------------------------------------------------------------------------
# 2. Логирование вызовов и параметров функции
from typing import Callable
from functools import wraps


def log_func(func: Callable):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"func {func.__name__} args {args} kwargs {kwargs}")
        res = func(*args, **kwargs)
        return res

    return wrapper


@log_func
def my_test_func(a: int, b: float, c="test"):
    return f"{a}, {b}, {c}"


my_test_func(1, 2, "one")
my_test_func(11, 12, c="tho")
my_test_func(5, 8, c="three")


# print(len(*filter(str.isupper,open("file2.txt").read())))


# ----------------------------------------------------------------------------
# Декоратор с параметром из списка кортежей (исключение, обработчик)
# Вызывает обработчик, при соответствующем исключении внутри оборачиваемой функции
from typing import Callable
from functools import wraps

def deco_param(ex_lst: list[tuple]):
    def inner_wrapper(func: Callable):
        @wraps(func)
        def wrapper(*args, **kwargs):
            nonlocal ex_lst
            try:
                res = func(*args, **kwargs)
                return res
            except Exception as ex:
                for eh in ex_lst:
                    if isinstance(ex, eh[0]):
                        return eh[1]()
                raise ex
        return wrapper
    return inner_wrapper

def zd_handler():
    print("Division by 0!")

@deco_param([(ZeroDivisionError, zd_handler)])
def test1(a, b):
    return a / b

test1(1, 0)
