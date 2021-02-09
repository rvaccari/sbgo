from tortoise import fields

from app.models.base import BaseModel


class OfferPackage(BaseModel):
    customer = fields.ForeignKeyField(
        "models.Customer", related_name="offer_packages_customer"
    )
    offers = fields.ReverseRelation["Offer"]
