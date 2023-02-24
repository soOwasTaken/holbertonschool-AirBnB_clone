#!/usr/bin/python3
"""Module that contain the City class"""
from models.base_model import BaseModel


class City(BaseModel):
    """Class define City"""
    state_id = str("")
    name = str("")
