from base64 import b64encode
from hashlib import sha256

import bcrypt


def hash_password(password: str) -> bytes:
    return bcrypt.hashpw(
        b64encode(sha256(password.encode("utf-8")).digest()),
        bcrypt.gensalt(),
    )


def compare_password(user_password: str, db_password: bytes) -> bool:
    return bcrypt.checkpw(
        b64encode(sha256(user_password.encode("utf-8")).digest()),
        db_password,
    )


def validate_password(password: str) -> tuple[bool, int]:
    """
    false, 1 = слишком короткий (мин 12)
    false, 2 = нет букв
    false, 3 = нет цифр
    true,  0 = норм всё (почти)
    """

    if len(password) < 12:
        return False, 1

    if not any(char.isalpha() for char in password):
        return False, 2

    if not any(char.isdecimal() for char in password):
        return False, 3

    return True, 0
