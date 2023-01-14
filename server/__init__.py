from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from server.controllers import api_router
from server.settings import settings
from server.utils.helpers.logger import logger
from starlette.responses import RedirectResponse
from tag_metadata import tags_metadata

app = FastAPI(
    openapi_tags=tags_metadata,
    title=settings.PROJECT_NAME,
    openapi_url=f"{settings.API_V1_STR}/openapi.json",
)

app.include_router(api_router, prefix=settings.API_V1_STR)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
async def startup():
    logger.info("Startup FastApi-Whisper")
    logger.info("http://127.0.0.1:8000")


@app.on_event("shutdown")
async def shutdown():
    logger.info("Shutdown Growyd-Server-Api")


@app.get(
    "/status",
    response_description="Check service health",
    tags=["root"]
)
async def index():
    return {
        "status": 'OK',
        "Message": 'API Whisper FastApi V1'
    }


@app.get(
    "/",
    response_description="Check service health",
    tags=["root"]
)
def main():
    return RedirectResponse(url='/docs/')


import server.whisper_v1 as whisper_v1
print(whisper_v1.__file__)
# import server.whisper_v2 as whisper_v2
# print(whisper_v2.__file__)
