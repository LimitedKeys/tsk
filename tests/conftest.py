import pytest

@pytest.fixture(scope='function')
def plan_a(tmpdir):
    path = tmpdir / 'plan_a.md'
    with open(path, 'w') as out:
        out.write('\n'.join([
            '# Plan',
            '',
            '## A',
            'Time: 12 h',
            'Tag: one',
            '',
            '## B',
            'Time: 16 h',
            'Tag: two',
            '',
            ]))
    return path

