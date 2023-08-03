from database import db
from models import User, Card, Account
from modules import create_user, get_user, update_user, delete_user


db.connect()

# Clean DB before populating it
db.drop_tables([User, Account, Card])

# Create new tables
db.create_tables([User, Account, Card])

# TODO: Populate DB

# Create User
print(create_user("Alonso Reyes", "alonssoreyes@gmail.com", "3312233456"))

# Get User
print(get_user(email="alonssoreyes@gmail.com"))

# Update user
print(update_user(email="alonssoreyes@gmail.com",
      new_values={'email': 'alonso.r@gmail.com'}))
print(get_user(email="alonso.r@gmail.com"))

# Delete User
print(delete_user(email="alonso.r@gmail.com"))
print(get_user(email="alonso.r@gmail.com"))
