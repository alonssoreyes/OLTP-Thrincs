from modules import *
from datetime import datetime

# Create all records on DB
populate_all()

print('***** Main.py *****\n\n')
#####################################
#Case 1 One Person dies, and all the money is transferred to the direct relative
print('***  Case 1 ***')
deceased_user = get_user(email='erick.martinez@gmail.com')
deceased_acc = get_account(user=deceased_user)
benefited_user = get_user(email='mike.castañeda@gmail.com')
benefited_acc = get_account(user=benefited_user)

## Last Balance on deceased
deceased_balance = deceased_acc.balance

## Update Benefited balance
benefited_balance = benefited_acc.balance
date = datetime.now()
update_acount(user = benefited_user, new_values={'balance':benefited_balance + deceased_balance})

## Register movements
create_movement(-deceased_balance, movementType='Transferencia', account=deceased_acc, date=date )
create_movement(deceased_balance, movementType='Transferencia', account=benefited_acc, date=date )

##Delete deceased account
delete_account(user=deceased_user)

print(f"Deceased user: {deceased_user}")
deceased_balance = "${:,.2f}".format(deceased_balance)
print(f"Deceased last balance: {deceased_balance}")
print(f"Benefited user: {benefited_user}")
benefited_balance = "${:,.2f}".format(benefited_balance)
print(f"Previous benefited balance = ${benefited_balance}")
new_balance = get_account(user=benefited_user).balance
new_balance =  "${:,.2f}".format(new_balance)
print(f"New benefited balance = { new_balance }")

#####################################


# gastamos y fondeamos
print('\n***  Case 2 ***')
test_user = get_user(email='pake.perez@gmail.com')
date = datetime.now()
test_account = get_account(user = test_user)
test_movement = create_movement(amount = 140000, movementType= "Abono", account = test_account, date = date)
print(get_movement(account=test_account, date=date))


print("*** FELICIDADES EQUIPO ***")
