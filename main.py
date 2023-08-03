from database import db
from models import User, Card, Account
from peewee import *
db.connect()

db.create_tables([User,Account, Card])


def create_user(name,email,phone):
    try:
        user = User(name=name,email=email,phone_number=phone)
        user.save()
        return user
    except IntegrityError:
        #User already exists
        return f"{email} is already in use"
    
def get_user(**kwargs):
    try:
        user = User.get(**kwargs)
        return user
    except User.DoesNotExist:
        print("User does not exists in database")
        return None


#TODO: Here you can create the rest of the functions


print(create_user("Alonso Reyes", "alonssoreyes@gmail.com","3312233456"))
print(get_user(email="alonssoreyes@gmail.com"))