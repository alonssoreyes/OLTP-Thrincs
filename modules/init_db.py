from database import db
from models import User, Card, Account
from .user import create_user, get_user
from .account import create_account

# TODO: Create records for all tables


def populate_all():
    db.connect()

    # Clean DB before populating it
    db.drop_tables([User, Account, Card])

    # Create new tables
    db.create_tables([User, Account, Card])

    print('****Create Users****')
    print(create_user("Alonso Reyes", "alonso.reyes@gmail.com", "3312233456"))
    print(create_user("Pake Perez", "pake.perez@gmail.com", "0000000001"))
    print(create_user("Jasmin Sanchez", "jasmin.sanchez@gmail.com", "0000000002"))
    print(create_user("Erick Martinez", "erick.martinez@gmail.com", "0000000003"))
    print(create_user("Mike Castañeda", "mike.castañeda@gmail.com", "0000000004"))

    print()
    print('****Create Accounts****')
    test_user = get_user(email='alonso.reyes@gmail.com')
    print(create_account(user=test_user, balance=63000))
    test_user = get_user(email='pake.perez@gmail.com')
    print(create_account(user=test_user, balance=100000))
    test_user = get_user(email='jasmin.sanchez@gmail.com')
    print(create_account(user=test_user, balance=3000))
    test_user = get_user(email='erick.martinez@gmail.com')
    print(create_account(user=test_user, balance=70000))
    test_user = get_user(email='mike.castañeda@gmail.com')
    print(create_account(user=test_user, balance=3000000))

    print('\n\n')
