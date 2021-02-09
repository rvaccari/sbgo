from app.models import Partner


async def get_or_create(partner_id: int, partner_name: str) -> Partner:
    partner, _ = await Partner.get_or_create(partner_id=partner_id, name=partner_name)
    return partner
