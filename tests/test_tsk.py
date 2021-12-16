
import pytest

import tsk

@pytest.fixture(scope='function')
def plan_a(tmpdir):
    path = tmpdir / 'plan_a.md'
    with open(path, 'w') as out:
        out.write('\n'.join([
            '# Plan',
            '',
            '## A',
            'Time: 12 h',
            '',
            '## B',
            'Time: 16 h',
            '',
            ]))
    return path

def test_parse_plan_a(plan_a):
    result = tsk.parse(plan_a)

    assert result.A.time == '12 h'
    assert result.B.time == '16 h'
