import logging

import uvicorn

from app.db import init_db
from app.main import create_application

logger = logging.getLogger(__name__)

application = create_application()


@application.on_event("startup")
async def startup_event():
    logger.info("Starting up...")
    init_db(application)


@application.on_event("shutdown")
async def shutdown_event():
    logger.info("Shutting down...")


if __name__ == "__main__":
    uvicorn.run(application, host="0.0.0.0", port=8000, log_level="debug")
