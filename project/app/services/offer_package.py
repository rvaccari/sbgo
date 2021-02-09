from typing import List

from app.models import Customer
from app.models.offer_package import OfferPackage
from app.repositories import offer as offer_repository
from app.repositories import offer_package as offer_package_repository
from app.repositories import partner as partner_repository
from app.schemas.offer import PartnerOfferOutSchema


async def create_from_partner_offers_schema(
    customer: Customer, partner_offers: List[PartnerOfferOutSchema]
) -> OfferPackage:
    offer_package = await offer_package_repository.create(customer)

    for partner_offer in partner_offers:
        partner = await partner_repository.get_or_create(
            partner_offer.partner_id, partner_offer.partner_name
        )
        await offer_repository.create(
            value=partner_offer.value,
            installments=partner_offer.installments,
            tax_rate_percent_monthly=partner_offer.tax_rate_percent_montly,
            total_value=partner_offer.total_value,
            offer_package=offer_package,
            partner=partner,
            customer=customer,
        )
    await offer_package.fetch_related("offers")
    return offer_package
