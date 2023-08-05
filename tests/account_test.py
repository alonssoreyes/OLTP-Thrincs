import pytest
from peewee import IntegrityError
from models import User, Account
from modules import create_account, get_account,update_acount,delete_account
from database import db

db.drop_tables([User,Account])
@pytest.fixture(scope='function')
def setup_db():
    db.create_tables([User, Account])

    yield  # This is where the testing happens

    db.drop_tables([User, Account])


def test_create_account(setup_db):

    user = User.create(name='Alonso Reyes', email='alonso.reyes@gmail.com', phone_number='3312233456')
    result = create_account(user=user, balance=20000)
    assert result.user == user
    assert result.balance == 20000
    result = create_account(user=user, balance=20000)
    assert result == "User already has an account"


def test_get_account(setup_db):

    user = User.create(name='Alonso Reyes', email='alonso.reyes@gmail.com', phone_number='3312233456')
    create_account(user=user, balance=20000)

    account = get_account(user=user)
    assert account is not None

    user2 = User.create(name='Alonso Reyes', email='alonso.reyes2@gmail.com', phone_number='3312233457')
    account = get_account(user=user2)
    assert account is None


def test_update_account(setup_db):

    user = User.create(name='Alonso Reyes', email='alonso.reyes@gmail.com', phone_number='3312233456')
    create_account(user=user, balance=20000)

    result = update_acount(user=user, new_values={'balance': 30000})
    assert result == "Account updated"
    account = get_account(user=user)
    assert account.balance == 30000



def test_delete_account(setup_db):
    user = User.create(name='Alonso Reyes', email='alonso.reyes@gmail.com', phone_number='3312233456')
    create_account(user=user, balance=20000)

    result = delete_account(user=user)
    assert result == 'Account for alonso.reyes@gmail.com deleted'

    account = get_account(user=user)
    assert account is None
