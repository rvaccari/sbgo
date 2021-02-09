import pytest
import responses

from app.config import get_settings
from app.models import Offer
from app.services import customer as customer_service


@pytest.fixture(autouse=True)
def mocked_responses():
    with responses.RequestsMock() as rsps:
        yield rsps


class TestServiceCustomerOffersFromExternalPartner:
    @pytest.mark.asyncio
    @responses.activate
    async def test_get_offers_from_partner(self, customer, partner_offers_payload):
        assert await Offer.all().count() == 0
        settings = get_settings()
        url = f"{settings.partner_host}/offers"
        responses.add(responses.POST, url=url, json=partner_offers_payload, status=200)

        offers = await customer_service.get_offers(customer.id)
        assert len(offers) == 5
