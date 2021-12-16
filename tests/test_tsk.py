
import pytest

import tsk

def test_parse_plan_a(plan_a):
    result = tsk.parse(plan_a)

    assert result.A.time == '12 h'
    assert result.B.time == '16 h'

TIME = [
    ('1 h',  1),
    ('1 d',  8),
    ('1 w',  40),
    ('1 y',  (52 * 40)),
]

@pytest.mark.parametrize("value,expected", TIME)
def test_str_to_hours(value, expected):
    actual = tsk.str_to_hours(value)
    assert actual == expected
