import pytest
from gugudan import get_result, print_gugudan, print_all_gugudan


def test_get_result_basic():
    assert get_result(3, 4) == 12
    assert get_result(5, 6) == 30
    assert get_result(7, 8) == 56


def test_get_result_boundary():
    assert get_result(2, 1) == 2
    assert get_result(9, 9) == 81


def test_get_result_all_tables():
    for n in range(2, 10):
        for m in range(1, 10):
            assert get_result(n, m) == n * m


def test_print_gugudan_output(capsys):
    print_gugudan(3)
    captured = capsys.readouterr()
    lines = captured.out.strip().split("\n")
    assert len(lines) == 9
    assert lines[0] == "3 x 1 = 3"
    assert lines[4] == "3 x 5 = 15"
    assert lines[8] == "3 x 9 = 27"


def test_print_gugudan_single_table(capsys):
    print_gugudan(5)
    captured = capsys.readouterr()
    lines = captured.out.strip().split("\n")
    assert len(lines) == 9
    assert lines[0] == "5 x 1 = 5"
    assert lines[8] == "5 x 9 = 45"


def test_print_all_gugudan_output(capsys):
    print_all_gugudan()
    captured = capsys.readouterr()
    lines = [l for l in captured.out.split("\n") if l.strip()]
    assert len(lines) == 72  # 8단 * 9줄
    assert lines[0] == "2 x 1 = 2"
    assert lines[71] == "9 x 9 = 81"
