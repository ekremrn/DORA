import io
import base64
from PIL import Image

def base64_to_image_array(input: str):
    image_bytes = base64.b64decode(input)
    image = Image.open(io.BytesIO(image_bytes))
    return image
