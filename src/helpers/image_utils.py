import base64

class ImageUtils:
    """This class will have useful functions"""

    def image_to_base64(image_bytes):
        """
        use it to convert images from fastapi to base64

        :param image_bytes: file recieved from UploadFile
        """

        encoded_image = base64.b64encode(image_bytes).decode("utf-8")
        
        return encoded_image
