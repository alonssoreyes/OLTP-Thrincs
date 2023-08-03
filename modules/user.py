from models import User
from peewee import *


def create_user(name, email, phone):
    try:
        user = User(name=name, email=email, phone_number=phone)
        user.save()
        return user
    except IntegrityError:
        # User already exists
        return f"{email} is already in use"


def get_user(**kwargs):
    try:
        user = User.get(**kwargs)
        return user
    except User.DoesNotExist:
        print("User does not exists in database")
        return None
