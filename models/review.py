#!/usr/bin/python3
"""Module that contain the Review class"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Class define Review"""
    place_id = str("")
    user_id = str("")
    text = str("")
