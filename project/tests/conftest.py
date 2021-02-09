import json
from typing import AsyncGenerator, Dict

import pytest
import responses
from asyncpg import ObjectInUseError
from starlette.testclient import TestClient
from tortoise import Tortoise
from tortoise.exceptions import DBConnectionError

from app import create_application
from app.config import Settings, get_settings
from app.models import Customer, Partner, Offer, OfferPackage


def get_settings_override():
    return Settings(
        testing=True,
        database_url=get_settings().database_url_test,
    )


@pytest.fixture(scope="function")
def test_app():
    app = create_application()
    app.dependency_overrides[get_settings] = get_settings_override

    with TestClient(app) as test_client:
        yield test_client


@pytest.fixture(autouse=True)
def mocked_responses():
    with responses.RequestsMock() as rsps:
        yield rsps


@pytest.fixture(scope="function", autouse=True)
@pytest.mark.asyncio
async def test_db() -> AsyncGenerator:
    """Initialize db connection before run test."""

    settings = get_settings()
    try:
        await Tortoise.init(db_url=settings.database_url_test, modules=settings.modules)
    except DBConnectionError:
        await Tortoise.init(
            db_url=settings.database_url_test,
            modules=settings.modules,
            _create_db=True,
        )
    await Tortoise.generate_schemas()

    yield

    try:
        await Tortoise._drop_databases()
    except ObjectInUseError:
        pass

    await Tortoise.close_connections()


@pytest.fixture
def customer_payload() -> Dict[str, any]:
    return {
        "cpf": "12345678901",
        "birth_date": "2000-01-01",
        "email": "foo@bar.com",
        "phone": "11 1111 1111",
        "salary": 1000.00,
    }


@pytest.fixture
@pytest.mark.asyncio
async def customer(customer_payload) -> Customer:
    customer = await Customer.create(**customer_payload)
    return customer


@pytest.fixture
def partner_1_payload() -> Dict[str, any]:
    return {
        "partner_id": "1",
        "name": "Parceiro 1",
    }


@pytest.fixture
@pytest.mark.asyncio
async def partner_1(partner_1_payload: Dict[str, any]) -> Partner:
    partner = await Partner.create(**partner_1_payload)
    return partner


@pytest.fixture
def partner_2_payload() -> Dict[str, any]:
    return {
        "partner_id": "2",
        "name": "Parceiro 2",
    }


@pytest.fixture
@pytest.mark.asyncio
async def partner_2(partner_2_payload: Dict[str, any]) -> Partner:
    partner = await Partner.create(**partner_2_payload)
    return partner


@pytest.fixture
def offer_1_payload() -> Dict[str, any]:
    return {
        "partner_id": 1,
        "partner_name": "Parceiro 1",
        "value": 10000,
        "installments": 24,
        "tax_rate_percent_montly": 2,
        "total_value": 12689.04,
    }


@pytest.fixture
def offer_2_payload() -> Dict[str, any]:
    return {
        "partner_id": 2,
        "partner_name": "Parceiro 2",
        "value": 12000,
        "installments": 36,
        "tax_rate_percent_montly": 2.2,
        "total_value": 17497.8,
    }


@pytest.fixture
@pytest.mark.asyncio
async def offer_2(offer_2_payload: Dict[str, any], partner_2: Partner) -> Offer:
    offer_2_payload.pop("partner_id")
    offer_2_payload.pop("partner_name")
    offer = await Offer.create(**dict({"partner": partner_2}, **offer_2_payload))
    return offer


@pytest.fixture
@pytest.mark.asyncio
async def offer_package(
    customer: Customer,
    partner_1: Partner,
    partner_2: Partner,
    offer_1_payload: Dict[str, any],
    offer_2_payload: Dict[str, any],
) -> OfferPackage:
    offer_package = await OfferPackage.create(customer=customer)

    await Offer.create(
        value=offer_1_payload.get("value"),
        installments=offer_1_payload.get("installments"),
        tax_rate_percent_monthly=offer_1_payload.get("tax_rate_percent_montly"),
        total_value=offer_1_payload.get("total_value"),
        offer_package=offer_package,
        partner=partner_1,
        customer=customer,
    )

    await Offer.create(
        value=offer_2_payload.get("value"),
        installments=offer_2_payload.get("installments"),
        tax_rate_percent_monthly=offer_2_payload.get("tax_rate_percent_montly"),
        total_value=offer_2_payload.get("total_value"),
        offer_package=offer_package,
        partner=partner_1,
        customer=customer,
    )

    return offer_package


@pytest.fixture
def partner_offers_payload() -> Dict:
    with open("tests/fixtures/partner_offers_payload.json") as fp:
        return json.load(fp)
