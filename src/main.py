from fastapi import FastAPI, APIRouter, UploadFile
from fastapi.responses import JSONResponse
from endpoints import base, upload


app = FastAPI()

app.include_router(base.pulse)
app.include_router(upload.upload)


