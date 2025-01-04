from app.calculations import add, subtract, multiply, devide, BankAccount, InsufficientFunds
import pytest

@pytest.fixture
def zero_bank_account():
    print("creating empty bank account")
    return BankAccount()


@pytest.fixture
def bank_account():
    return BankAccount(50)

@pytest.mark.parametrize("num1, num2, result", [
    (1, 2, 3), 
    (3, 5, 8), 
    (12, 5, 17)
])
def test_add(num1, num2, result):
    print("testing add functions.")
    sum = add(num1, num2)
    assert sum == result
def test_subtract():
    print("testing subtract functions.")
    assert subtract(2, 1) == 1
def test_multiply():
    print("testing multiply functions.")
    assert multiply(2, 1) == 2
def test_devide():
    print("testing devide functions.")
    assert devide(10, 5) == 2

def test_bank_set_initial_amount(bank_account):

    assert bank_account.balance == 50


def test_bank_default_amount(zero_bank_account):
    print("testing my bank account")
    assert zero_bank_account.balance == 0


def test_withdraw(bank_account):

    bank_account.withdraw(20)
    assert bank_account.balance == 30


def test_deposit(bank_account):

    bank_account.deposit(30)
    assert bank_account.balance == 80


def test_collect_interest(bank_account):

    bank_account.collect_interest()
    assert round(bank_account.balance, 6) == 55


@pytest.mark.parametrize("deposited, withdrew, expected", [
    (200, 100, 100),
    (50, 10, 40),
    (1200, 200, 1000)

])
def test_bank_transaction(zero_bank_account, deposited, withdrew, expected):
    zero_bank_account.deposit(deposited)
    zero_bank_account.withdraw(withdrew)
    assert zero_bank_account.balance == expected


def test_insufficient_funds(bank_account):
    with pytest.raises(InsufficientFunds):
        bank_account.withdraw(200)