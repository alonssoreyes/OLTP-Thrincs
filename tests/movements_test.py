import pytest
from peewee import IntegrityError
from models import Account, User, Movements
from database import db
from modules import create_user, create_account, create_movement, get_movement, update_movement, delete_movement
from datetime import datetime

db.drop_tables([Account, User, Movements])
date = datetime.now()

def test_create_movement():
    #Init account
    db.create_tables([Account, User, Movements])
    user = create_user("Pake Perez", "pake.perez@gmail.com", "0000000009")
    acc = create_account(user=user, balance=10000)
    

    # Intenta crear un usuario
    result = create_movement(500,'Deposito',acc, date)
    assert result.amount == 500
    assert result.account.user.name == 'Pake Perez'
    assert result.movementType == 'Deposito'
    assert result.date == date

    db.drop_tables([Account, User, Movements])

def test_get_movement():
    #Init movement
    db.create_tables([Account, User, Movements])
    user = create_user("Pake Perez", "pake.perez@gmail.com", "0000000009")
    acc = create_account(user=user, balance=10000)
    mov = create_movement(500,'Deposito',acc, date)

    # Intenta obtener el usuario
    result = get_movement(account=acc, date=date)
    assert result == mov

    # Intenta obtener un usuario que no existe
    result = get_movement(account=acc, date=datetime.now())
    assert result is None

    db.drop_tables([Account, User, Movements])

def test_update_movement():
    #Init movement
    db.create_tables([Account, User, Movements])
    user = create_user("Pake Perez", "pake.perez@gmail.com", "0000000009")
    acc = create_account(user=user, balance=10000)
    mov = create_movement(500,'Deposito',acc, date)

    # Actualiza el nombre del usuario
    new_amount = 1000
    result = update_movement(account=acc, date=date, new_values={'amount':new_amount})
    assert result == 'Movement updated'

    # Verifica que el nombre se haya actualizado
    mov = get_movement(account=acc, date=date)
    assert mov.amount == new_amount

    db.drop_tables([Account, User, Movements])

def test_delete_movement():
    #Init movement
    db.create_tables([Account, User, Movements])
    user = create_user("Pake Perez", "pake.perez@gmail.com", "0000000009")
    acc = create_account(user=user, balance=10000)
    mov = create_movement(500,'Deposito',acc, date)

    # Elimina el usuario
    result = delete_movement(acc, date)
    assert result == f'Movement {mov.id} deleted'

    # Verifica que el usuario se haya eliminado
    user = get_movement(account=acc, date=date)
    assert user is None

    db.drop_tables([Account, User, Movements])

