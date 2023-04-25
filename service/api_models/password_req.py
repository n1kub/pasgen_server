from pydantic import BaseModel


class PasswordRequest(BaseModel):
    password_length: int
    with_special_symbols: bool
    has_upper: bool
    password_to_modify: str
