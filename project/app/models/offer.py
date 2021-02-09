from tortoise import fields

from app.models.base import BaseModel


class Offer(BaseModel):
    value = fields.DecimalField(14, 2)
    installments = fields.SmallIntField()
    tax_rate_percent_monthly = fields.DecimalField(3, 2)
    total_value = fields.DecimalField(14, 2)
    offer_package = fields.ForeignKeyField("models.OfferPackage", related_name="offers")
    partner = fields.ForeignKeyField("models.Partner", related_name="offers_partner")
    customer = fields.ForeignKeyField("models.Customer", related_name="offers_customer")
