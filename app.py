from fastapi import FastAPI
from fastapi.responses import JSONResponse
from schema.user_input import UserInput
from schema.prediction_response import PredictionResponse
from model.predict import predict_output,model,MODEL_VERSION


app = FastAPI()

# human readabe      
@app.get('/')
def home():
    return {'message':'Insurance Premium Prediction API'}
# machine readavle ye endpoint tabb banaya hai ke hum isko cloud services par deploy kar sakon 
@app.get('/health')
def health_check():
    return {
        'Status': 'OK', 
        'version': MODEL_VERSION,
        'model_loaded': model is not None
    }

@app.post('/predict',response_model=PredictionResponse)
def predict_premium(data: UserInput):

    user_input ={
        'bmi': data.bmi,
        'age_group': data.age_group,
        'lifestyle_risk': data.lifestyle_risk,
        'city_tier': data.city_tier,
        'income_lpa': data.income_lpa,
        'occupation': data.occupation
    }
    try:

        prediction = predict_output(user_input)

        return JSONResponse(status_code=200, content={'response': prediction})
    except Exception as e:
        return JSONResponse(status_code=500,content=str(e))