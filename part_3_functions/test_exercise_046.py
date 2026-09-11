import pytest
from part_3_functions.exercise_046 import log_call

def test_log_call_decorator(capsys):
    @log_call
    def say_hello(name):
        return f"Hello, {name}"

    result = say_hello("World")

    assert result == "Hello, World"

    captured = capsys.readouterr()
    output = captured.out.strip()
    assert "Calling function 'say_hello'..." in output
    assert "Function 'say_hello' finished." in output
