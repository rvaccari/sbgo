import fastapi

from app.schemas.health import HealthOutSchema

router = fastapi.APIRouter()


@router.get("/", response_model=HealthOutSchema)
def health():
    return HealthOutSchema(status="OK")
