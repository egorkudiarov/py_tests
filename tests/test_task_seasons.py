import pytest

from task_seasons import check_month

@pytest.mark.parametrize(
    'mouth, expected',
    ((1, 'Зима'),
     (4, 'Весна'),
     (18, 'Некорректный номер месяца'),
    )
)
def test_ideal_conditions(mouth, expected):
    result = check_month(mouth)
    assert result == expected

def test_incorrect_input_string():
    month = 'a'
    excepted_error = TypeError
    raised_error = None
    try:
        result = check_month(month)
    except Exception as _error:
        raised_error = _error
    assert excepted_error == raised_error.__class__
