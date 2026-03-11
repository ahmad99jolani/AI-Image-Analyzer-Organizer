from helpers.config import Settings, get_settings
from fastapi import UploadFile

#AppCofig: Settings = get_settings()

class ValidateData:

    def validate_upload_file(file: UploadFile, AppCofig: Settings):
        if file.content_type not in AppCofig.IMAGE_TYPE:
            return False, "File Format Not Allowed"
        if file.size > AppCofig.IMAGE_SIZE:
            return False, "File Size Not Accepted"
        else:
            return True, "File Got Passed The Validation"
        

