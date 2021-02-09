from typing import List

from app.config import get_settings
from app.models import Offer
from app.repositories import customer as customer_repository
from app.repositories import offer_package as offer_package_repository
from app.services import offer_package as offer_package_service
from external_services.partner import client as partner_client


async def get_offers(customer_id) -> List[Offer]:
    settings = get_settings()
    customer = await customer_repository.get(customer_id)
    offer_package = await offer_package_repository.get_from_cache(
        customer, settings.minutes_cache_offer
    )
    if offer_package and len(offer_package.offers) > 0:
        return offer_package.offers

    external_offers = await partner_client.request_offers(customer)
    offer_package = await offer_package_service.create_from_partner_offers_schema(
        customer=customer, partner_offers=external_offers
    )
    return offer_package.offers
