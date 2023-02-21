#!/usr/bin/python3
""" AirBnB clone - The console"""
from .base_model import BaseModel


class place(BaseModel):
    """Define the review class"""
    place_id: str = ""
    user_id: str = ""
    text: str = ""
