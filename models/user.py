#!/usr/bin/python3
"""
user module
"""
from models.base_model import BaseModel, Base, Table, Column, String
from sqlalchemy.orm import relationship, backref
import hashlib
from os import getenv


class User(BaseModel, Base):
    """
    User class attribute
    """
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        __tablename__ = "users"
        email = Column(String(128), nullable=False)
        _password = Column("password", String(128), nullable=False)
        first_name = Column(String(128), nullable=True)
        last_name = Column(String(128), nullable=True)
        reviews = relationship("Review", backref="user",
                               cascade="all, delete, delete-orphan")
        places = relationship("Place", backref="user",
                              cascade="all, delete, delete-orphan")
    else:
        email = ""
        password = ""
        first_name = ""
        last_name = ""

    def __init__(self, *args, **kwargs):
        """
        initializes from the BaseModel
        """
        value = kwargs.get("password", "")
#        kwargs["password"] = hashlib.md5(bytes(value.encode('utf-8')))
        super().__init__(*args, **kwargs)

    @property
    def password(self):
        return self.__dict__.get('_password', "")

    @password.setter
    def password(self, value):
        """
        hash the password

        Argument:
           value: password new value
        """
        b = bytes(value.encode("utf-8"))
        self.__dict__['_password'] = hashlib.md5(b).hexdigest()
