import os
import pandas as pd

from tqdm import tqdm
from PIL import Image
from dotenv import load_dotenv

from pymongo.server_api import ServerApi
from pymongo.mongo_client import MongoClient

from ai import search_engine as se

load_dotenv()

DATABASE_URI = str(os.getenv("DATABASE_URI"))
DATABASE_NAME = str(os.getenv("DATABASE_NAME"))
DATABASE_COLLECTION = str(os.getenv("DATABASE_COLLECTION"))

CLIENT = MongoClient(DATABASE_URI, server_api=ServerApi("1"))
DB = CLIENT[DATABASE_NAME]
COLLECTION = DB[DATABASE_COLLECTION]

JSONPATH = str(os.getenv("JSONPATH"))
IMAGESPATH = str(os.getenv("IMAGESPATH"))

DATA = pd.read_json(path_or_buf=JSONPATH, orient="records")

process = tqdm(
    DATA.iterrows(), desc="Extracting...", ncols=100, colour="green", total=len(DATA)
)
for _, row in process:
    row = row.to_dict()
    if COLLECTION.find_one({"id": row.get("id")}):
        continue
    if any(row.get(key) is None for key in row.keys()):
        continue
    if row.get("thumb_image").get("path") is None:
        continue

    # Image Feature
    image_path = os.path.join(IMAGESPATH, row.get("thumb_image").get("path"))

    if not os.path.exists(image_path):
        continue

    # Feature Vector Extraction
    image = Image.open(image_path)
    feature = se.__get_feat(image)

    if feature is None:
        continue

    row.update({"feature": feature.tolist()[0]})

    # Insert to DB
    COLLECTION.insert_one(row)
