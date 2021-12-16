import tsk

def test_parse_plan_a(plan_a):
    result = tsk.parse(plan_a)

    assert result.A.time == '12 h'
    assert result.B.time == '16 h'
