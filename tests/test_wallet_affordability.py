import pytest

from src.wallet_affordability import can_afford


@pytest.mark.parametrize(
    "balance, price, expected",
    [
        (1000, 500, True),  # testing balance higher than price           (error)
        (500, 500, True),  # testing balance equal to price               (error)
        (0, 0, True),  # testing zero price with zero balance             (error)
        (499, 500, False),  # testing balance 1 cent below price          (error)
    ],
)
def test_valid_input_returns_expected_bool(balance, price, expected):
    result = can_afford(balance, price)

    # "is" rejects 1 and 0: only a real True or False passes
    assert result is expected


@pytest.mark.parametrize(
    "balance, price",
    [
        (-1, 0),  # testing negative balance
        (1000, -1),  # testing negative price
    ],
)
def test_negative_input_raises_value_error(balance, price):
    with pytest.raises(ValueError):
        can_afford(balance, price)


@pytest.mark.parametrize(
    "balance, price",
    [
        (1000.0, 500),  # testing float balance
        ("1000", 500),  # testing string balance
        (True, 500),  # testing bool balance (bool is not a valid int)
        (1000, 500.0),  # testing float price
        (1000, "500"),  # testing string price
        (1000, True),  # testing bool price
        ("1000", -5),  # testing wrong type and bad value together (TypeError first)
    ],
)
def test_invalid_type_raises_type_error(balance, price):
    with pytest.raises(TypeError):
        can_afford(balance, price)
