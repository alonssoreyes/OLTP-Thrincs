from database import db
from models import User, Card, Account
from modules import *


db.connect()

# Clean DB before populating it
db.drop_tables([User, Account, Card])

# Create new tables
db.create_tables([User, Account, Card])

# TODO: Populate DB

print('****User****')
# Create User
print(create_user("Alonso Reyes", "alonssoreyes@gmail.com", "3312233456"))

# Get User
print(get_user(email="alonssoreyes@gmail.com"))

# Update user
print(update_user(email="alonssoreyes@gmail.com",
      new_values={'email': 'alonso.r@gmail.com'}))
print(get_user(email="alonso.r@gmail.com"))

# Delete User
# print(delete_user(email="alonso.r@gmail.com"))
# print(get_user(email="alonso.r@gmail.com"))


# Create account
print('\n****Account****')
test_user = get_user(email="alonso.r@gmail.com")
print(create_account(user=test_user, balance=100000))

# Get account
print(get_account(user=test_user))

# Update account
print(update_acount(user=test_user, new_values={'balance': 5000}))
print(get_account(user=test_user))

# Delete account
print(delete_account(user=test_user))
print(get_account(user=test_user))
