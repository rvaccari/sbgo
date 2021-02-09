from pydantic import BaseModel


class HealthOutSchema(BaseModel):
    status: str
