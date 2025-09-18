import os
import tempfile

from src.decorators import log

with tempfile.NamedTemporaryFile(delete=False) as temp_file:
    temp_filename = temp_file.name


@log(filename=temp_filename)
def log_correct(x, y):
    return x * y


def test_log_correct(capsys):
    result = log_correct(4, 2)
    assert result == 8
    captured = capsys.readouterr()
    assert f"log_correct ок. Результат: 8.\n" in captured.out


@log(filename=temp_filename)
def log_no_args():
    """Проверка на отсутствие аргументов"""
    return "No arguments"


def test_log_no_args(capsys):
    result = log_no_args()
    assert result == "No arguments"
    captured = capsys.readouterr()
    assert f"log_no_args ок. Результат: {result}." in captured.out


@log(filename=temp_filename)
def log_except():
    """Проверка обработки других исключений"""
    return {"a": 1}["b"]


def test_log_except(capsys):
    log_except()
    captured = capsys.readouterr()
    assert "log_except error: 'b'. Inputs: (), {}" in captured.out


@log(filename=temp_filename)
def lod_diff_arg(a, b):
    """Проверка с разными типами аргументов"""
    return a + b


def test_lod_diff_arg(capsys):
    result = lod_diff_arg("Python ", "the best")
    assert result == "Python the best"
    captured = capsys.readouterr()
    assert f"lod_diff_arg ок. Результат: Python the best.\n" in captured.out


@log(filename="test_log.txt")
def log_add(x, y):
    return x + y


# Тестовая функция


def test_log_success():
    if os.path.exists("test_log.txt"):
        os.remove("test_log.txt")
    log_add(3, 4)
    with open("test_log.txt", "r", encoding="utf-8") as log_file:
        log_content = log_file.read()
    assert "log_add ок. Результат: 7.\n" in log_content


def test_file_cleanup():
    filename = "test_log_cleanup.txt"

    @log(filename=filename)
    def log_cleanup(x):
        """Проверка очистки файла"""
        return x

    log_cleanup(1)
    assert os.path.exists(filename)
    os.remove(filename)
    assert not os.path.exists(filename)
