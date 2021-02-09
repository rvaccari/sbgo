import json

import pytest
import responses

from app.config import get_settings


class TestCustomerPost:
    def test_post_customer_success(self, test_app, customer_payload):
        response = test_app.post(
            "/api/v1/customers/", data=json.dumps(customer_payload)
        )
        response.raise_for_status()

        assert response.status_code == 201
        assert customer_payload.items() <= response.json().items()

    def test_post_customer_no_payload(self, test_app):
        response = test_app.post("/api/v1/customers/")

        assert response.status_code == 422


class TestCustomerOffer:
    @pytest.mark.asyncio
    @responses.activate
    def test_get_offers_from_customer(
        self, test_app, mocked_responses, customer, partner_offers_payload
    ):
        settings = get_settings()

        responses.add(
            responses.POST,
            url=f"{settings.partner_host}/offers",
            json=partner_offers_payload,
            status=200,
        )
        url = f"/api/v1/customers/{customer.id}/offers/"
        response = test_app.get(url)
        response.raise_for_status()

        assert response.status_code == 200
