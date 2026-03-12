from fastapi import FastAPI, APIRouter, UploadFile
from fastapi.responses import JSONResponse
from endpoints import health, upload


app = FastAPI()

app.include_router(health.pulse)
app.include_router(upload.upload)


