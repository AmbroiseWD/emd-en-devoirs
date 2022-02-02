import pytest
from unittest import mock
from is_it_xmas import is_it_xmas

from datetime import date


@pytest.mark.parametrize("_date,expected",
                         [(date(2022, 12, 24), True),
                          (date(2018, 11, 12), False)])
@mock.patch("is_it_xmas.date")
def test_should_return_true_on_xmas_day(mock_date, _date, expected):
    mock_date.today.return_value = _date
    assert is_it_xmas() == expected
