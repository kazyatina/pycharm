import inspect
from datetime import datetime
from functools import wraps
from typing import Callable, Tuple, Any, Dict


def log(filename=None) -> Callable[[Any], Callable[[tuple[Any, ...], dict[str, Any]], None]]:
    """Декоратор для логирования информации о вызовах функций.
    Возвращает обертку, которая записывает имя функции, результат её выполнения,
    время выполнения и информацию об ошибках, если они возникают."""

    def wrapped(func) -> Callable[[tuple[Any, ...], dict[str, Any]], None]:
        @wraps(func)
        def inner(*args, **kwargs) -> None:
            result = None

            try:
                result = func(*args, **kwargs)
                start_time = datetime.now()
                end_time = datetime.now()
                log_message = (
                    f"Функция: {func.__name__}\n"
                    f"Результат: {result}\n"
                    f"Время начала: {start_time}\n"
                    f"Время выполнения: {end_time - start_time}\n"
                    f"Время окончания: {end_time}\n"
                )
                if filename:
                    with open(filename, "a") as log_file:
                        log_file.write(log_message)
                        print(log_message)
                else:
                    print(log_message)
            except Exception as e:
                start_time = datetime.now()
                end_time = datetime.now()
                log_message = (
                    f"Функция: {func.__name__}\n"
                    f"Ошибка: {e}\n"
                    f"Входные параметры: {inspect.getcallargs(func, *args, **kwargs)}\n"
                    f"Время выполнения: {end_time - start_time}\n"
                )
                if filename:
                    with open(filename, "a") as log_file:
                        log_file.write(log_message)
                        print(log_message)
                else:
                    print(log_message)

            return result

        return inner

    return wrapped


@log(filename="mylog.txt")
def example(x: int, y: int) -> float:
    """После декорирования возвращает имя функции, результат и время выполнения"""
    return x / y


# try:
#     example()  # Вызовет TypeError и декоратор его обработает
# except Exception as e:
#     print(f"Выявлено исключение в основном коде: {e}")

# example(35, 5)
