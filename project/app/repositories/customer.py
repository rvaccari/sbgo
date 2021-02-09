from uuid import UUID

from app.models.customer import Customer
from app.schemas.customer import CustomerInSchema


async def create(payload: CustomerInSchema) -> Customer:
    customer = await Customer.create(**payload.dict())
    return customer


async def get(customer_id: UUID) -> Customer:
    customer = await Customer.get(id=customer_id)
    return customer
