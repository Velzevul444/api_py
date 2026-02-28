from pydantic import BaseModel, Field, field_validator
import re


class Numbers(BaseModel):
    num1: float
    num2: float


class User(BaseModel):
    name: str
    id: int


class User_2(BaseModel):
    name: str
    age: int


class Feedback(BaseModel):
    name: str = Field(
        ...,
        min_length=2,
        max_length=50,
        description="Имя отправителя от 2 до 50 символов"
    )

    message: str = Field(
        ...,
        min_length=10,
        max_length=500,
        description="Текст отзыва от 10 до 500 символов"
    )

    @field_validator("name")
    @classmethod
    def validate_name(cls, v: str) -> str:
        v = v.strip()
        if len(v) < 2 or len(v) > 50:
            raise ValueError("Имя должно содержать от 2 до 50 символов")
        return v

    @field_validator("message")
    @classmethod
    def validate_message(cls, v: str) -> str:
        forbidden_words = ["кринж", "рофл", "вайб"]
        message_lower = v.lower()

        for word in forbidden_words:
            pattern = r"\b" + re.escape(word) + r"\w*\b"
            if re.search(pattern, message_lower):
                raise ValueError("Использование недопустимых слов")

        return v