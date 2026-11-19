import pytest

from src.wallet_withdrawal import withdraw


@pytest.mark.parametrize(
    "balance, amount, expected",
    [
        (1000, 300, 700),  # testing normal withdrawal
        (1000, 1, 999),  # testing smallest valid withdrawal (1 cent)
    ],
)
def test_valid_withdrawal_returns_remaining_balance(balance, amount, expected):
    result = withdraw(balance, amount)

    assert result == expected


def test_withdraw_exact_balance_returns_zero():
    result = withdraw(1000, 1000)  # testing withdrawing the whole balance (error)

    assert result == 0


@pytest.mark.parametrize(
    "balance, amount",
    [
        (1000, 0),  # testing zero amount
        (1000, -1),  # testing negative amount
        (-1, 1),  # testing negative balance
        (1000, 1001),  # testing amount 1 cent more than balance
    ],
)
def test_withdraw_out_of_range_input_raises_value_error(balance, amount):
    with pytest.raises(ValueError):
        withdraw(balance, amount)


@pytest.mark.parametrize(
    "balance, amount",
    [
        (1000.0, 100),  # testing float balance
        ("1000", 100),  # testing string balance
        (True, 100),  # testing bool balance (bool is not a valid int)
        (1000, 100.0),  # testing float amount
        (1000, "100"),  # testing string amount
        (1000, True),  # testing bool amount
        ("1000", -5),  # testing wrong type and bad value together (TypeError first)
    ],
)
def test_withdraw_invalid_type_raises_type_error(balance, amount):
    with pytest.raises(TypeError):
        withdraw(balance, amount)