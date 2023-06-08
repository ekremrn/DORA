import io
import base64
from PIL import Image


def base64_to_image_array(input: str):
    image_bytes = base64.b64decode(input)
    image = Image.open(io.BytesIO(image_bytes))
    return image



def image_to_base64(image):
    buffered = io.BytesIO()
    image.save(buffered, format="PNG")
    image_bytes = buffered.getvalue()
    encoded_image = base64.b64encode(image_bytes).decode("utf-8")
    return encoded_image
