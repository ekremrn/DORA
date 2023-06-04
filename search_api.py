# Import necessary modules
import os

from tqdm import tqdm
from typing import Dict
from fastapi import FastAPI
from dotenv import load_dotenv

from torch import Tensor
from ai import search_engine as se
from helpers.data_handlers import base64_to_image_array

from pymongo.server_api import ServerApi
from pymongo.mongo_client import MongoClient

# Load environment variables
load_dotenv()

# Set MongoDB connection variables using environment variables
DATABASE_URI = str(os.getenv("DATABASE_URI"))
DATABASE_NAME = str(os.getenv("DATABASE_NAME"))
DATABASE_COLLECTION = str(os.getenv("DATABASE_COLLECTION"))

# Connect to MongoDB and retrieve data
CLIENT = MongoClient(DATABASE_URI, server_api=ServerApi("1"))
DB = CLIENT[DATABASE_NAME]
COLLECTION = DB[DATABASE_COLLECTION]

# Convert MongoDB data to a dictionary with "id" and "feature" keys
DATA = [row for row in tqdm(COLLECTION.find({}, {"_id": 1, "feature": 1}))]
DATA = {
    "_id": [row.get("_id") for row in DATA],
    "feature": Tensor([row.get("feature") for row in DATA]),
}

# Initialize FastAPI app
app = FastAPI()

# Define a POST endpoint to perform image search
@app.post("/search")
def search(input: Dict):
    # Convert base64-encoded image data to an array
    image = base64_to_image_array(input.get("data"))
    # Perform image search using the search_engine module
    output = se.search(image, DATA.get("feature"))
    # Retrieve the IDs of the search results
    ids = [DATA.get("_id")[i] for i in output.get("indices")]
    # Retrieve data from MongoDB for the search results
    data_list = list(COLLECTION.find({"_id": {"$in": ids}}, {"feature": 0, "_id": 0}))
    # Return the search results as a list of dictionaries
    return data_list
