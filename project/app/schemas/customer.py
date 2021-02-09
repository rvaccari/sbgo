import re
from datetime import date
from decimal import Decimal

from pydantic import BaseModel, validator
from tortoise.contrib.pydantic import pydantic_model_creator

from app.models import Customer

CustomerOutSchema = pydantic_model_creator(
    Customer, name="Customer", exclude=("created_at", "updated_at")
)


class CustomerInSchema(BaseModel):
    cpf: str
    birth_date: date
    email: str
    phone: str
    salary: Decimal

    @validator("cpf")
    def cpf_validate(cls, value):
        cpf = re.sub(r"\D", "", value)
        if len(cpf) != 11:
            raise ValueError("CPF must contain 11 digits")
        return cpf
