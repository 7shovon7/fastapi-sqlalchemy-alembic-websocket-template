from contextlib import asynccontextmanager

from fastapi import FastAPI

from api.config import Settings
from api.public import api as public_api
from api.utils.logger import logger_config


logger = logger_config(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("Startup: triggered")

    yield

    logger.info("Shutdown: triggered")


def create_app(settings: Settings):
    app = FastAPI(
        title=settings.PROJECT_NAME,
        version=settings.VERSION,
        docs_url='/docs',
        description=settings.DESCRIPTION,
        lifespan=lifespan,
    )

    app.include_router(public_api)
    
    return app
