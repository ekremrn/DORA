import os
import pickle

from torch import Tensor
from dotenv import load_dotenv

load_dotenv()
DATAPATH = str(os.getenv("DATAPATH"))
PICKLE_PATH = os.path.join(DATAPATH, "data.pickle")

with open(PICKLE_PATH, 'rb') as f:
    PRODUCTS = pickle.load(f)
    
FEATURES = Tensor([product.get("feat") for product in PRODUCTS])
