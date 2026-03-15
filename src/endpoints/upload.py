from fastapi import APIRouter, UploadFile, status, Request, Depends, File
from fastapi.responses import JSONResponse
from helpers.config import get_settings, Settings
from helpers import ImageUtils, FileUtils
from controllers import ValidateData
from services import OpenaiService
import os
import logging

#logger = logging.getLogger('uvicorn.error')


upload = APIRouter(
    prefix="/upload",
    tags=["image","proccessing_files"]
)
#app_settings: Settings = get_settings()

@upload.post('/')
async def upload_file(file: UploadFile = File(...),
                    app_settings:Settings = Depends(get_settings)):

    valid_status, valid_message =  ValidateData.validate_upload_file(file=file, AppCofig= app_settings)

    # for tracing: enable below line to print out the values
    #return file._in_memory
    #return file.content_type, file.size, valid_status, valid_message

    if valid_status == False:
        return JSONResponse(
            status_code=406,
            content={
                "message": valid_message
            }
        )

    image_bytes = await file.read()

    image_base64 = ImageUtils.image_to_base64(image_bytes=image_bytes)

    #--------------- Calling LLM ---------------#

    service_OpenAI = OpenaiService()

    image_description, image_category, image_summary = service_OpenAI.analyze_image(base64_image=image_base64)

    #--------------- saving file locally ---------------#

    #return image_description, image_category, image_summary , FileUtils.generate_file_name(file.filename.split(".")[0], image_summary, file.content_type.split('/')[-1])
    Save_status = FileUtils.save_image_locally(image_binary= image_bytes,
                                               folder_name=image_category,
                                               image_name=file.filename.split(".")[0],
                                               image_summary=image_summary,
                                               image_ext=file.content_type.split('/')[-1])
    
    #return image_description, image_category, image_summary, Save_status
    
    return JSONResponse(status_code=200,
                        content={
                            "description": image_description,
                            "category": image_category,
                            "summary": image_summary,
                            "save_status": Save_status
                        }
    )



    

        


