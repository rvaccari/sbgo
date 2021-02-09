from tortoise import fields

from app.models.base import BaseModel


class Partner(BaseModel):
    partner_id = fields.CharField(max_length=255, unique=True)
    name = fields.CharField(max_length=255)
