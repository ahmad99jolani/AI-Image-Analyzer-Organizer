from pydantic import BaseModel

class Imagescheme(BaseModel):
    
    image_description: str
    image_category: str
    image_summary_3_words: str

