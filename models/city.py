#!/usr/bin/python3
""" AirBnB clone - The console"""
from .base_model import BaseModel


class City(BaseModel):
    """Define the City class"""
    state_id = str("")
    name = str("")
