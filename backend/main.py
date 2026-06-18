from fastapi import FastAPI, UploadFile, File
from PIL import Image, UnidentifiedImageError
from model import load_model
from predict import predict_image
import io

app = FastAPI()

model = load_model()

classes = [
    'Pepper__bell___Bacterial_spot',
    'Pepper__bell___healthy',
    'Potato___Early_blight',
    'Potato___Late_blight',
    'Potato___healthy',
    'Tomato_Bacterial_spot',
    'Tomato_Early_blight',
    'Tomato_Late_blight',
    'Tomato_Leaf_Mold',
    'Tomato_Septoria_leaf_spot',
    'Tomato_Spider_mites_Two_spotted_spider_mite',
    'Tomato__Target_Spot',
    'Tomato__Tomato_YellowLeaf__Curl_Virus',
    'Tomato__Tomato_mosaic_virus',
    'Tomato_healthy'
]

@app.get("/")
def home():
    return {
        "message": "Plant Disease Detection API is running"
    }

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    
    try:
        contents = await file.read()

        print("\n===== NEW REQUEST =====")
        print("Filename:", file.filename)
        print("Content Type:", file.content_type)
        print("Bytes Received:", len(contents))

        image = Image.open(
            io.BytesIO(contents)
        ).convert("RGB")

        result = predict_image(
            image,
            model,
            classes
        )

        return result

    except UnidentifiedImageError:
        return {
            "error": "Uploaded file is not a valid image."
        }

    except Exception as e:
        print("ERROR:", str(e))

        return {
            "error": str(e)
        }