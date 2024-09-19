#!/usr/bin/python3
"""Module to generate random users"""

from faker import Faker
from typing import List
import logging
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
logging.basicConfig(filename=BASE_DIR / 'user.log' , level=logging.DEBUG)

fake = Faker()

def get_user() -> str:
    """_Method that creates a new single user_

    Returns:
        str: _A new user_
    """
    logging.info("Generating user")
    user = f"{fake.first_name()} {fake.last_name()}"
    return user

def get_users(nb_users : int = 0) -> list:
    """_Method that creates nb_users_

    Args:
        nb_users (int, optional): _description_. Defaults to 0.

    Returns:
        list of created users_
    """
    logging.info(f"Generating a list of {nb_users} users")
    i = 0
    n_users = []
    while i < nb_users:
        user = get_user()
        n_users.append(user)
        i += 1
    return n_users # ==  [get_user() for _ in range(nb_users)]


if __name__ == "__main__":
    users = get_users(nb_users=5)
    print(users)
