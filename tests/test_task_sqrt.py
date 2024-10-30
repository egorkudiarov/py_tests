import pytest

from task_sqrt import solution, discriminant

@pytest.mark.parametrize(
    'a, b, c, expected',
    ((1, 8, 15, (-3.0, -5.0)),
     (1, -13, 12, (12.0, 1.0)),
     (-4, 28, -49, 3.5),
     (1, 1, 1, 'корней нет'),
    )
)
def test_solution_ideal_conditions(a, b, c, expected):
    result = solution(a, b, c)
    assert result == expected

def test_discriminant_incorrect_input():
    a, b, c = 1, 2, 'v'
    excepted_error = TypeError
    raised_error = None
    try:
        result = discriminant(a, b, c)
    except Exception as _error:
        raised_error = _error
    assert excepted_error == raised_error.__class__

def test_solution_incorrect_input():
    a, b, c = 1, 2, 'v'
    excepted_error = TypeError
    raised_error = None
    try:
        result = solution(a, b, c)
    except Exception as _error:
        raised_error = _error
    assert excepted_error == raised_error.__class__

def test_solution_division_by_zero():
    a, b, c = 0, 2, 3
    excepted_error = ZeroDivisionError
    raised_error = None
    raised_error = None
    try:
        result = solution(a, b, c)
    except Exception as _error:
        raised_error = _error
    assert excepted_error == raised_error.__class__