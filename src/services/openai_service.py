from openai import OpenAI
from helpers.config import get_settings, Settings
from services.schemes.openai_schemas import Imagescheme 

AppCofig: Settings = get_settings()

class OpenaiService:

    """
    This class is to init calls with openai
    """        

    def __init__(self):
        self.client =  OpenAI(api_key=AppCofig.OPENAI_API_KEY)

    def analyze_image(self, base64_image, prompt="what's in this image? The 'image_category' must be ONE WORD ONLY") -> Imagescheme:

        try:
            response = self.client.chat.completions.parse(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "user",
                    "content": [
                        { "type": "text", "text": prompt },
                        {
                            "type": "image_url",
                            "image_url":{
                            "url": f"data:image/jpeg;base64,{base64_image}",
                            "detail": "low"
                            }
                        },
                    ],
                }
            ],
            response_format = Imagescheme,
            #text_format=Imagescheme,
            max_tokens=6000
            )

            #return response
            #return response.choices[0].message.content
            #return Imagescheme.model_validate_json(response.choices[0].message.content)
            response_scheme = Imagescheme.model_validate_json(response.choices[0].message.content)
            return response_scheme.image_description, response_scheme.image_category, response_scheme.image_summary_3_words

        except Exception as e:
            return {"error": str(e)}
        
        
        

