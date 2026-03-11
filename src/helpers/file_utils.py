import os
import re
import shutil 
from pathlib import Path

class FileUtils:

    @staticmethod
    def save_image_locally(image_binary, folder_name, image_name, image_summary, image_ext):

        base_dir= os.path.dirname(os.path.dirname(__file__))
        uploads_dir= os.path.join(base_dir, "uploads")

        folder_path = os.path.join(uploads_dir, folder_name)
        #print(folder_path)

        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
        #os.makedirs(save_dir, exist_ok=True)

        generated_filename: str = FileUtils.generate_file_name(image_name=image_name,image_summary=image_summary, image_ext=image_ext)
        full_path = os.path.join(folder_path, generated_filename)
        
        try:
            with open(full_path, "wb") as f:
                f.write(image_binary)
            return f'image save successfully to: {folder_path}', f'Image saved with this name: {generated_filename}'

        except Exception as e:
            error_msg = f" Error saving image: {str(e)}"
            print(error_msg)
            return error_msg

    @staticmethod
    def generate_file_name(image_name: str, image_summary: str, image_ext:str):

        image_name = re.sub(r'[^A-Za-z0-9_.-]', '', image_name)
        return f'{image_name}_{image_summary.replace(" ","_")}.{image_ext}'
