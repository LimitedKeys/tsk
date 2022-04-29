
import numpy as np
import pytest

import tsk

import summary_configs

def test_parse_plan_a(plan_a):
    result = tsk.parse(plan_a)

    assert result[(plan_a, 'A')]["time"] == 12
    assert result[(plan_a, 'A')]["tag"] == "one"

    assert result[(plan_a, 'B')]["time"] == 16
    assert result[(plan_a, 'B')]["tag"] == "two"

TIME = [
    ('0.1 h', 0.1),
    ('0.5 h', 0.5),
    ('0.25 h', 0.25),
    ('1.5 h', 1.5),
    ('1H',    1),
    ('1 h',   1),
    ('1h1h',  2),
    ('1 D',   8),
    ('1w',   40),
    ('1y',   (52 * 40)),
    ('1Y1W', (53 * 40)),
]

@pytest.mark.parametrize("value,expected", TIME)
def test_str_to_hours(value, expected):
    actual = tsk.str_to_hours(value)
    assert actual == expected

STR = [
    (0.1,   '0.1 h'),
    (0.5,   '0.5 h'),
    (1.1,   '1.1 h'),
    (1.5,   '1.5 h'),
    (1,     '1 h'),
    (7,     '7 h'),
    (8,     '1 d'),
    (15,    '1 d 7 h'),
    (39,    '4 d 7 h'),
    (40,    '1 w'),
    (41,    '1 w 1 h'),
    (48,    '1 w 1 d'),
    (52*40, '1 y'),
]

@pytest.mark.parametrize("value,expected", STR)
def test_hours_to_str(value, expected):
    actual = tsk.hours_to_str(value)
    assert actual == expected

@pytest.mark.parametrize("expected_summary,expected_total,tag_in", summary_configs.CONFIGS)
def test_summary(expected_total, expected_summary, tag_in):
    summary_dict = {}
    for (path, tag, name, time) in expected_summary:
        summary_dict[(path, name)] = {
            "tag":tag,
            "time":time
        }

    total, summary = tsk.summerize(summary_dict, tag_in)

    np.testing.assert_equal(total, expected_total)
    if tag_in:
        filtered_summary = [i for i in expected_summary if tag_in in i[1]]
        np.testing.assert_equal(summary, filtered_summary)
    else:
        np.testing.assert_equal(summary, expected_summary)
