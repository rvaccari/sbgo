import logging

from fastapi import FastAPI, APIRouter

from app.apis.v1 import customer
from app.views import default

logger = logging.getLogger(__name__)


def init_routes(app: FastAPI):
    router = APIRouter()
    router.include_router(customer.router, prefix="/customers", tags=["customers"])
    app.include_router(router, prefix="/api/v1")

    app.include_router(default.router)


def create_application() -> FastAPI:
    app = FastAPI(title="Seu Barriga Gerador de Ofertas", docs_url="/swagger/")

    init_routes(app)

    return app
