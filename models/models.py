from peewee import *
from database import db


class BaseModel(Model):
    class Meta:
        database = db


class User(BaseModel):
    name = CharField()
    email = CharField(unique=True)
    phone_number = CharField()

    def __str__(self) -> str:
        return f"User {self.id}: {self.name} <{self.email}>"

    def get_email(self):
        return self.email


class Account(BaseModel):
    user = ForeignKeyField(User, backref='accounts')
    balance = DecimalField(default=0.0)

    def __str__(self) -> str:
        balance = "${:,.2f}".format(self.balance)
        return f"Account {self.id}: {self.user.email} <{balance}>"


class Card(BaseModel):
    account = ForeignKeyField(Account, backref='cards')
    security_code = CharField(default='1111')    
    card_number = CharField(unique=True)
    holder_name = CharField()

    def __str__(self) -> str:
        return f"Card {self.id}: Account {self.account.id}, Holder Name: {self.holder_name}, Card Number: {self.card_number}, Security Code: {self.security_code}"

class Movements(BaseModel):
    amount = DecimalField()
    account = ForeignKeyField(Account, backref='cards')
    movementType = CharField() #Deposito o gasto
