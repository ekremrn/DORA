from PIL import Image

from torch.nn.functional import cosine_similarity
from transformers import ViTImageProcessor, ViTModel

image_processor = ViTImageProcessor.from_pretrained('google/vit-base-patch16-224-in21k')
model = ViTModel.from_pretrained('google/vit-base-patch16-224-in21k')

def __get_feat(image):
    inputs = image_processor(images=image, return_tensors="pt") 
    output = model(**inputs).pooler_output
    return output

def search(image_input, features, first = 20):
    feat = __get_feat(image_input)
    sorted_similarities = cosine_similarity(features, feat).sort(descending=True)
    result = {
        "indices" : sorted_similarities.indices.tolist()[:first],
        "ratios"  : sorted_similarities.values.tolist()[:first]
    }
    return result
