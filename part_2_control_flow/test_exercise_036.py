import pytest
from part_2_control_flow.exercise_036 import robust_read_file

def test_robust_read_file_exists(tmp_path, capsys):
    p = tmp_path / "test.txt"
    p.write_text("Hello")

    content = robust_read_file(str(p))
    assert content == "Hello"
    captured = capsys.readouterr()
    assert "File operation finished." in captured.out


def test_robust_read_file_not_exists(capsys):
    content = robust_read_file("non_existent_file.txt")
    assert content is None
    captured = capsys.readouterr()
    assert "File operation finished." in captured.out
