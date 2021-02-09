from decimal import Decimal
from typing import List

from pydantic import BaseModel
from tortoise.contrib.pydantic import pydantic_model_creator, pydantic_queryset_creator

from app.models.offer import Offer

OfferOutSchema = pydantic_model_creator(Offer, name="Offer")
OfferList = pydantic_queryset_creator(Offer, name="OfferList")


class OfferListOutSchema(BaseModel):
    count: int
    items: List[OfferOutSchema]


class PartnerOfferOutSchema(BaseModel):
    partner_id: int
    partner_name: str
    value: Decimal
    installments: int
    tax_rate_percent_montly: Decimal
    total_value: Decimal
