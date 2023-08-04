from models import User
from peewee import IntegrityError
import pytest
#Object should be a user instnace
user = User(name="Alonso", email="a@ibm.com", phone_number="2232343")
user.id = 1000
def test_user_instance():
    assert isinstance(user,User)


#Should create an user instance
def test_user_object():
    assert user.email == "a@ibm.com"
    assert user.name == "Alonso"
    assert user.phone_number == "2232343"


def test_user_already_exists():
    User.create(email="paquito@ibm.com",name="paquito",phone_number="33244")

    with pytest.raises(IntegrityError):
        User.create(email="paquito@ibm.com",name="paquito",phone_number="33244")
    
    
def test_user_update():
    pass