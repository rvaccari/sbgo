import logging
from typing import List

import httpx
from pydantic import parse_obj_as

from app.config import get_settings
from app.models import Customer
from app.schemas.offer import PartnerOfferOutSchema

logger = logging.getLogger(__name__)


async def request_offers(customer: Customer) -> List[PartnerOfferOutSchema]:
    base_log = f"Get offers from customer id: "
    logger.info(f"{base_log} - start")

    settings = get_settings()
    timeout = settings.partner_timeout
    url = f"{settings.partner_host}/offers"

    async with httpx.AsyncClient() as client:
        response = await client.post(url, timeout=timeout)

    logger.info(f"{base_log} - received data, status {response.status_code}.")
    response.raise_for_status()

    partner_offers = parse_obj_as(
        List[PartnerOfferOutSchema], response.json().get("offers")
    )

    return partner_offers
