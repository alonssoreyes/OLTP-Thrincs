from modules import *
from datetime import datetime

# Create all records on DB
populate_all()

print('*** Main.py ***')
test_user = get_user(email='pake.perez@gmail.com')
print(get_account(user=test_user))
update_acount(user=test_user, new_values={'balance': 50})
print(get_account(user=test_user))

# gastamos y fondeamos
date = datetime.now()
test_account = get_account(user = test_user)
test_movement = create_movement(amount = 140000, movementType= "Abono", account = test_account, date = date)
print(get_movement(account=test_account, date=date))


print("*** FELICIDADES EQUIPO ***")
