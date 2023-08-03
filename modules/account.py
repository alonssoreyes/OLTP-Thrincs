from models import Account
from peewee import *


def create_account(user, balance):
    try:
        acc = Account(user=user, balance=balance)
        acc.save()
        return acc
    except IntegrityError:
        # Account already exists
        return "User already has an account"


def get_account(**kwargs):
    try:
        acc = Account.get(**kwargs)
        return acc
    except Account.DoesNotExist:
        print("Account does not exists in database")
        return None


def update_acount(user, new_values):
    if not new_values:
        print("Invalid parameters")
        return None

    try:
        query = Account.update(new_values).where(user == user)
        query.execute()

        return 'Account updated'

    except Account.DoesNotExist:
        print("Account does not exists in database")
        return None

    except ValueError as e:
        print('Account could not be updated: ')
        print(e.args[0])
        return None


def delete_account(user):
    try:
        acc = Account.get(user=user)
        acc.delete_instance()
        return 'Account for' + user.get_email() + ' deleted'
    except Account.DoesNotExist:
        print("User does not exists in database")
        return None
