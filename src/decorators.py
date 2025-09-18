from datetime import datetime
from functools import wraps


def log(filename=None):
    """Декоратор для логирования информации о вызовах функций.
    Возвращает обертку, которая записывает имя функции, результат её выполнения,
    время выполнения и информацию об ошибках, если они возникают."""

    def wrapped(func):
        @wraps(func)
        def inner(*args, **kwargs):
            try:
                start_time = datetime.now()
                result = func(*args, **kwargs)
                end_time = datetime.now()
                work_time = end_time - start_time
                log_message = f"{func.__name__} ок. Результат: {result}.\n"

                if filename:
                    with open(filename, "a", encoding="utf-8") as log_file:
                        log_file.write(log_message)
                        print(log_message)
                        print(f"Время начала:{start_time}. Время окончания:{end_time}. Длительность :{work_time}")

            except Exception as e:
                result = None
                log_message = f"{func.__name__} error: {e}. Inputs: {args}, {kwargs}\n"
                if filename:
                    with open(filename, "a", encoding="utf-8") as log_file:
                        log_file.write(log_message)
                        print(log_message)

            return result

        return inner

    return wrapped


@log(filename="mylog.txt")
def example(x: int, y: int) -> float:
    """После декорирования возвращает имя функции, результат и время выполнения"""
    return x / y


example(35, 5)
