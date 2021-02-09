from datetime import datetime, timedelta

import pytest
from freezegun import freeze_time

from app.models import OfferPackage
from app.repositories import offer_package as offer_package_repository


@pytest.mark.asyncio
async def test_get_cached_offers(offer_package: OfferPackage):
    offer_package_db = await offer_package_repository.get_from_cache(
        offer_package.customer
    )
    assert len(offer_package_db) == 2


@pytest.mark.asyncio
async def test_no_offers_after_cache_expires(offer_package: OfferPackage):
    expired_cache = datetime.utcnow() + timedelta(minutes=20)
    with freeze_time(expired_cache):
        offer_package_db = await offer_package_repository.get_from_cache(
            offer_package.customer
        )
        assert not offer_package_db
