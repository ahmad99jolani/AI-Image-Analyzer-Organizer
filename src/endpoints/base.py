from fastapi import APIRouter, UploadFile, status, Request, Depends
from fastapi.responses import JSONResponse
from helpers.config import get_settings, Settings


pulse = APIRouter(
    prefix="/test",
    tags=["image","connection"]
)
#app_settings: Settings = get_settings()

@pulse.get('/')
async def test_connection(app_settings:Settings = Depends(get_settings)):
    return JSONResponse(
        status_code=200,
        content={
            "status": "alive",
            "App Name": app_settings.APP_NAME,
            "App Version": app_settings.APP_VERSION
        }
    )

