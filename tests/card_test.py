import pytest
from peewee import IntegrityError
from models import Card, Account, User
from database import db
from modules import assign_new_card, create_user, create_account, get_card_by_number, update_nip, cancel_card

db.drop_tables([Card, User, Account])

def test_assign_new_card():
    db.create_tables([Card, Account, User])
    user = create_user("Pake Perez", "pake.perez@gmail.com", "0000000009")
    acc = create_account(user=user, balance=10000)

    # Asigna card
    result = assign_new_card(acc, user.name)
    assert result.holder_name == 'Pake Perez'
    assert result.account.id == 1
    assert result.security_code == '1111'
    assert result.card_number is not None

    db.drop_tables([User, Account, Card])

def test_get_card():
    #Init a new card
    db.create_tables([Card, Account, User])
    user = create_user("Pake Perez", "pake.perez@gmail.com", "0000000009")
    acc = create_account(user=user, balance=10000)
    card = assign_new_card(acc, user.name)

    # Intenta obtener una tarjeta
    result = get_card_by_number(card.card_number)
    assert result.card_number == str(card.card_number)

    # Intenta obtener una tarjeta que no existe
    result = get_card_by_number(1234567812345678)
    assert result is None

    db.drop_tables([Card, User, Account])


def test_update_nip():
    #Init a new card
    db.create_tables([Card, Account, User])
    user = create_user("Pake Perez", "pake.perez@gmail.com", "0000000009")
    acc = create_account(user=user, balance=10000)
    card = assign_new_card(acc, user.name)

    # Actualiza el nip de la tarjeta
    new_nip = '1234'
    result = update_nip(card.card_number, new_nip)
    assert result == "NIP updated"

    # Verifica que el nip se actualizo
    card = get_card_by_number(card.card_number)
    assert card.security_code == new_nip

    db.drop_tables([Card, User, Account])


def test_cancel_card():
    #Init a new card
    db.create_tables([Card, Account, User])
    user = create_user("Pake Perez", "pake.perez@gmail.com", "0000000009")
    acc = create_account(user=user, balance=10000)
    card = assign_new_card(acc, user.name)

    # Elimina la card
    result = cancel_card(card.id)
    assert result == f'Card {card.id} has been deleted'

    # Verifica que la card se haya eliminado
    card = get_card_by_number(card.card_number)
    assert card is None

    db.drop_tables([Card,User,Account])
