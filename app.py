from fastapi import FastAPI
from fastapi.responses import JSONResponse
from schema.user_input import UserInput
import pickle
import pandas as pd 
from model.predict import predict_output,model,MODEL_VERSION

#import the ml model 
with open('model/model.pkl','rb') as f:
    model = pickle.load(f)

MODEL_VERSION = '1.0.0'

app = FastAPI()

#human readable 
@app.get('/')  
def home():
    return {'message': "Insurance premium prediction api"}

#machine readable
@app.get('/health')
def health_check():
    return{
        'status':'OK', 
        'version': MODEL_VERSION,
        'model_loaded': model is not None

    }

@app.post('/predict')
def predict_premium(data: UserInput):

    user_input = {
        'bmi':data.bmi,
        'age_group': data.age_group,
        'lifestyle_risk': data.lifestyle_risk,
        'city_tier': data.city_tier,
        'income_lpa':data.income_lpa,
        'occupation': data.occupation
    }

    try:
        prediction = predict_output(user_input)

        return JSONResponse(status_code=200, content={'predicted_category': prediction})

    except Exception as e:

        return JSONResponse(status_code=500, content=str(e))