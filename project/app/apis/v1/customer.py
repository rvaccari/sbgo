from uuid import UUID

from fastapi import APIRouter

from app.repositories import customer as customer_repository
from app.schemas.customer import CustomerInSchema, CustomerOutSchema
from app.schemas.offer import OfferListOutSchema, OfferOutSchema
from app.services import customer as customer_service

router = APIRouter()


@router.post("/", response_model=CustomerOutSchema, status_code=201)
async def new_customer(payload: CustomerInSchema) -> CustomerOutSchema:
    customer = await customer_repository.create(payload)
    response = await CustomerOutSchema.from_tortoise_orm(customer)
    return response


@router.get("/{customer_id}/offers/", status_code=200)
async def get_offers(customer_id: UUID) -> OfferListOutSchema:
    offers = await customer_service.get_offers(customer_id)
    offers_out = [await OfferOutSchema.from_tortoise_orm(o) for o in offers]
    response = OfferListOutSchema(count=len(offers), items=offers_out)
    return response
