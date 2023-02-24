from random import choice, getrandbits
import string


def generate_new_password(length: int, has_uppercase: bool, has_special_symbols: bool) -> str:
    new_pass = ""
    if has_special_symbols and has_uppercase:
        characters = string.ascii_letters + string.digits + string.punctuation
        return new_pass.join(choice(characters) for _ in range(length))
    elif has_uppercase:
        return new_pass.join(choice(string.ascii_letters) for _ in range(length))
    elif has_special_symbols:
        characters = string.ascii_lowercase + string.digits + string.punctuation
        return new_pass.join(choice(characters) for _ in range(length))
    else:
        return new_pass.join(choice(string.ascii_lowercase) for _ in range(length))


def update_password(old_password: str, add_uppercase: bool, add_special_symbols: bool) -> str:
    new_pass = old_password.lower()
    special_characters = string.digits + string.punctuation
    if add_uppercase and add_special_symbols:
        for char in old_password:
            new_pass.join(char.upper() if bool(getrandbits(1)) else char)
            new_pass.join(choice(special_characters) if bool(getrandbits(1)) else "")
        return new_pass
    elif add_special_symbols:
        for _ in old_password:
            new_pass.join(choice(special_characters) if bool(getrandbits(1)) else "")
        return new_pass
    elif add_uppercase:
        for char in old_password:
            new_pass.join(char.upper() if bool(getrandbits(1)) else char)
        return new_pass
    else:
        return new_pass

    