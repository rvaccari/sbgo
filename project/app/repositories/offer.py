from decimal import Decimal

from app.models import Customer, Partner, OfferPackage, Offer


async def create(
    value: Decimal,
    installments: int,
    tax_rate_percent_monthly: Decimal,
    total_value: Decimal,
    offer_package: OfferPackage,
    partner: Partner,
    customer: Customer,
) -> Customer:
    offer = await Offer.create(
        value=value,
        installments=installments,
        tax_rate_percent_monthly=tax_rate_percent_monthly,
        total_value=total_value,
        offer_package=offer_package,
        partner=partner,
        customer=customer,
    )
    return offer
