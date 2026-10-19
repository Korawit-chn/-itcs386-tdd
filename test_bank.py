# test_bank.py
import pytest
from bank import BankAccount, InsufficientFunds

@pytest.fixture
def account():
    return BankAccount("alice", balance=100)

def test_deposit_increases_balance(account):
    account.deposit(50)
    assert account.balance == 150

def test_withdraw_more_than_balance_is_refused(account):
    with pytest.raises(InsufficientFunds):
        account.withdraw(500)
    assert account.balance == 100

def test_each_test_gets_a_fresh_account(account):
    assert account.balance == 100

def test_deposit_zero_value(account):
    with pytest.raises(ValueError, match="deposit must be positive"):
        account.deposit(0)
    assert account.balance == 100

def test_withdraw_whole_balance(account):
    account.withdraw(100)
    assert account.balance == 0

def test_two_withdraws_reduce_both_balance(account):
    account.withdraw(50)
    account.withdraw(25)
    assert account.balance == 25

def test_interest(account):
    account.add_interest(0.10)
    assert account.balance == pytest.approx(110)