from modules import *

# Create all records on DB
populate_all()

print('*** Main.py ***')
test_user = get_user(email='pake.perez@gmail.com')
print(get_account(user=test_user))
update_acount(user=test_user, new_values={'balance': 50})
print(get_account(user=test_user))

