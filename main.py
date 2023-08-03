from database import db
from models import User, Card, Account
from modules import create_user, get_user

db.connect()

db.create_tables([User, Account, Card])

# TODO: Populate DB
print(create_user("Alonso Reyes", "alonssoreyes@gmail.com", "3312233456"))
print(get_user(email="alonssoreyes@gmail.com"))
