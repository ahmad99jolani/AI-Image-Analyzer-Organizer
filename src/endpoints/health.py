from fastapi import APIRouter, UploadFile, status, Request, Depends
from fastapi.responses import JSONResponse
from helpers.config import get_settings, Settings


pulse = APIRouter(
    prefix="/health",
    tags=["Health"]
)
#app_settings: Settings = get_settings()

@pulse.get('/')
async def health_check(app_settings:Settings = Depends(get_settings)):
    return JSONResponse(
        status_code=200,
        content={
            "status": "UP",
            "app_name": app_settings.APP_NAME,
            "app_version": app_settings.APP_VERSION,
        }
    )

