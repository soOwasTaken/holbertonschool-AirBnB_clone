#!/usr/bin/python3
""" AirBnB clone - The console"""
from .base_model import BaseModel


class State(BaseModel):
    """Define the State class"""
    name: str = ""
