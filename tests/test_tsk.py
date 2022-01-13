
import pytest

import tsk

def test_parse_plan_a(plan_a):
    result = tsk.parse(plan_a)

    assert result.A.time == 12
    assert result.A.tag  == "one"
    assert result.B.time == 16
    assert result.B.tag  == "two"

TIME = [
    ('1H',   1),
    ('1 h',  1),
    ('1h1h', 2),
    ('1 D',  8),
    ('1w',  40),
    ('1y',  (52 * 40)),
    ('1Y1W', (53 * 40)),
]

@pytest.mark.parametrize("value,expected", TIME)
def test_str_to_hours(value, expected):
    actual = tsk.str_to_hours(value)
    assert actual == expected

STR = [
    (1,  '1 h'),
    (7,  '7 h'),
    (8,  '1 d'),
    (15, '1 d 7 h'),
    (39, '4 d 7 h'),
    (40, '1 w'),
    (41, '1 w 1 h'),
    (48, '1 w 1 d'),
    (52*40, '1 y'),
]

@pytest.mark.parametrize("value,expected", STR)
def test_hours_to_str(value, expected):
    actual = tsk.hours_to_str(value)
    assert actual == expected
