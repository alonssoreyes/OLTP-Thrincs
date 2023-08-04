from models import Card, Movements
from peewee import *

#General Actions
#Depositos
#Gastos

def save_movement(amount, movementType, account): #se puede quitar o no usar
    card = Card.get(Card.card_number==account)
    movement = Movements(amount = amount, movementType=movementType, account = account)
    movement.save()
    print(f'Movement from Account: {movement} Amount :{amount} Movement Type: {movementType}')
    pass

def create_movement(amount, movementType, account):
    try:
        movement = Movements(amount = amount, movementType=movementType, account = account)
        movement.save()
        return movement
    except:
        return "Something went wrong"

def get_movement(account):
    try:
        movement = Movements(account = account)
        print('Movements: ')
        print(movement)
    except:
        return "Something went wrong"

def delete_movement():

    pass