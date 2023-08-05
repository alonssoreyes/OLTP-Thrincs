import pytest
from peewee import IntegrityError
from models import User, Account
from database import db
from modules import create_user, get_user, update_user, delete_user

def test_create_user():
    db.create_tables([User])

    # Intenta crear un usuario
    result = create_user('Alonso Reyes','alonso.reyes@gmail.com','3312233456')
    assert result.name == 'Alonso Reyes'
    assert result.email == 'alonso.reyes@gmail.com'
    assert result.phone_number == '3312233456'

    # Intenta crear otro usuario con el mismo email, debería fallar
    result = create_user('Alonso Reyes','alonso.reyes@gmail.com','3312233457')
    assert result == "alonso.reyes@gmail.com is already in use"

    db.drop_tables([User])


def test_get_user():
    db.create_tables([User])

    # Crea un usuario
    user = User.create(name='Alonso Reyes', email='alonso.reyes@gmail.com', phone_number='3312233456')

    # Intenta obtener el usuario
    result = get_user(email='alonso.reyes@gmail.com')
    assert result == user

    # Intenta obtener un usuario que no existe
    result = get_user(email='noexiste@gmail.com')
    assert result is None

    db.drop_tables([User])


def test_update_user():
    db.create_tables([User])

    # Crea un usuario
    User.create(name='Alonso Reyes', email='alonso.reyes@gmail.com', phone_number='3312233456')

    # Actualiza el nombre del usuario
    result = update_user(email='alonso.reyes@gmail.com', new_values={'name': 'Alonso'})
    assert result == 'User updated'

    # Verifica que el nombre se haya actualizado
    user = get_user(email='alonso.reyes@gmail.com')
    assert user.name == 'Alonso'

    db.drop_tables([User])


def test_delete_user():
    db.create_tables([User])

    # Crea un usuario
    User.create(name='Alonso Reyes', email='alonso.reyes@gmail.com', phone_number='3312233456')

    # Elimina el usuario
    result = delete_user(email='alonso.reyes@gmail.com')
    assert result == 'User alonso.reyes@gmail.com deleted'

    # Verifica que el usuario se haya eliminado
    user = get_user(email='alonso.reyes@gmail.com')
    assert user is None

    db.drop_tables([User])
