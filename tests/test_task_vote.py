import pytest

from task_vote import vote

@pytest.mark.parametrize(
    'input_list, expected',
    (([1,1,1,2,3], 1),
     ([1,2,3,2,2], 2),
    )
)
def test_ideal_conditions(input_list, expected):
    result = vote(input_list)
    assert result == expected

@pytest.mark.xfail
def test_incorrect_input_string():
    input_string = 'asdzxca'
    excepted_error = TypeError
    raised_error = None
    try:
        result = vote(input_string)
    except Exception as _error:
        raised_error = _error
    assert excepted_error == raised_error.__class__

@pytest.mark.xfail
def test_incorrect_input_not_int_in_list():
    input_list = [1, 2, 3, 1, 'a']
    excepted_error = TypeError
    raised_error = None
    try:
        result = vote(input_list)
    except Exception as _error:
        raised_error = _error
    assert excepted_error == raised_error.__class__

@pytest.mark.xfail
def test_incorrect_output_not_int():
    input_list = [1, 2, 3, 'a', 'a']
    result = vote(input_list)
    assert isinstance(result, int)