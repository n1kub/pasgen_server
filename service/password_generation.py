import logging
import string
from logging.config import dictConfig
from random import choice, getrandbits

from my_logger import LogConfig

dictConfig(LogConfig().dict())
logger = logging.getLogger("mylogger")


def generate_new_password(length: int, has_uppercase: bool, has_special_symbols: bool) -> str:
    logger.debug(f"Generation started")
    new_pass = ""
    if has_special_symbols and has_uppercase:
        characters = string.ascii_letters + string.digits + string.punctuation
        logger.debug(f"Generation finished")
        return new_pass.join(choice(characters) for _ in range(length))
    elif has_uppercase:
        logger.debug(f"Generation finished")
        return new_pass.join(choice(string.ascii_letters) for _ in range(length))
    elif has_special_symbols:
        characters = string.ascii_lowercase + string.digits + string.punctuation
        logger.debug(f"Generation finished")
        return new_pass.join(choice(characters) for _ in range(length))
    else:
        logger.debug(f"Generation finished")
        return new_pass.join(choice(string.ascii_lowercase) for _ in range(length))


def randomly_make_upper(char: str):
    return char.upper() if bool(getrandbits(1)) else char


def randomly_get_special_char():
    special_characters = string.digits + string.punctuation
    return (choice(special_characters)) if bool(getrandbits(1)) else ""


def update_password(old_password: str, add_uppercase: bool, add_special_symbols: bool) -> str:
    logger.debug(f"Modifying started")

    if add_uppercase and add_special_symbols:
        new_pass = "".join(randomly_make_upper(char) for char in old_password.lower())
        new_pass = "".join((char + randomly_get_special_char()) for char in new_pass)
        logger.debug(f"Modifying finished")
        return new_pass
    elif add_special_symbols:
        new_pass = "".join((char + randomly_get_special_char()) for char in old_password.lower())
        logger.debug(f"Modifying finished")
        return new_pass
    elif add_uppercase:
        new_pass = "".join(randomly_make_upper(char) for char in old_password.lower())
        logger.debug(f"Modifying finished")
        return new_pass
    else:
        logger.debug(f"Modifying finished")
        return old_password.lower()
