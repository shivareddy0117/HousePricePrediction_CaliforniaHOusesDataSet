import logging
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
import numpy as np


from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import joblib
import numpy as np

app = FastAPI()

# Add the CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Rest of your code...

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Load the trained model and scaler
model = joblib.load('linear_regression_model.pkl')
scaler = joblib.load('scaler.pkl')

# In-memory storage for house features
houses = {}

class HouseFeatures(BaseModel):
    MedInc: float
    HouseAge: float
    AveRooms: float
    AveBedrms: float
    Population: float
    AveOccup: float
    Latitude: float
    Longitude: float

@app.get('/house/{house_id}')
async def get_house(house_id: int):
    if house_id not in houses:
        raise HTTPException(status_code=404, detail="House not found")
    return houses[house_id]

@app.put('/house/{house_id}')
async def update_house(house_id: int, house_features: HouseFeatures):
    houses[house_id] = house_features
    return {"status": "House features updated", "house_id": house_id}

@app.delete('/house/{house_id}')
async def delete_house(house_id: int):
    if house_id not in houses:
        raise HTTPException(status_code=404, detail="House not found")
    del houses[house_id]
    return {"status": "House features deleted", "house_id": house_id}

@app.post('/predict')
async def predict_house_price(house_features: HouseFeatures):
    try:
        # Scale the input features
        scaled_features = scaler.transform(np.array([[
            house_features.MedInc,
            house_features.HouseAge,
            house_features.AveRooms,
            house_features.AveBedrms,
            house_features.Population,
            house_features.AveOccup,
            house_features.Latitude,
            house_features.Longitude
        ]]))

        # Make the prediction
        predicted_price = model.predict(scaled_features)[0]

        return {'predicted_price': predicted_price}
    except Exception as e:
        logger.error(f"Error while making prediction: {e}")
        return {'error': str(e)}
