from tortoise import fields

from app.models.base import BaseModel


class Customer(BaseModel):
    cpf = fields.CharField(max_length=11, index=True, unique=True)
    birth_date = fields.DateField()
    email = fields.CharField(max_length=255)
    phone = fields.CharField(max_length=30)
    salary = fields.DecimalField(14, 2)
