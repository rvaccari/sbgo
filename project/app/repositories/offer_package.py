from datetime import timedelta, datetime
from typing import Optional

from tortoise.query_utils import Q

from app.models import Customer
from app.models.offer_package import OfferPackage


async def get_from_cache(
    customer: Customer, minutes_cache: int
) -> Optional[OfferPackage]:
    cache_date = datetime.utcnow() - timedelta(minutes=minutes_cache)
    offer_package = (
        await OfferPackage.filter(
            Q(customer__id=customer.id), Q(created_at__gt=cache_date)
        )
        .prefetch_related("offers")
        .order_by("-created_at")
        .first()
    )

    if not offer_package or not offer_package.offers:
        return None

    return offer_package


async def create(customer: Customer) -> OfferPackage:
    offer_package = await OfferPackage.create(customer=customer)
    return offer_package
