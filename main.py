from typing import Dict
from fastapi import FastAPI

import search_engine as ise
from data import FEATURES
from helpers import base64_to_image_array

app = FastAPI()

@app.post("/search")
def search(input: Dict):
    image = base64_to_image_array(input.get("data"))
    output = ise.search(image, FEATURES)
    return output

