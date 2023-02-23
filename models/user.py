#!/usr/bin/python3
""" AirBnB clone - The console"""
from .base_model import BaseModel


class User(BaseModel):
    """
    Define the User class
    """

    email = str("")
    password = str("")
    first_name = str("")
    last_name = str("")
