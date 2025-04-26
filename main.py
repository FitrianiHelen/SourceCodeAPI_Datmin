from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class StudentData(BaseModel):
    math_score: float
    reading_score: float
    writing_score: float
    gender: str  # 'male' atau 'female'

@app.post('/predict')
def predict_performance(data: StudentData):
    # Hitung average score
    average_score = (data.math_score + data.reading_score + data.writing_score) / 3

    if data.gender.lower() == 'female':
        threshold = 65  # Misal threshold lebih ringan sedikit
    else:
        threshold = 66  # Threshold default
    
    # Prediksi Excellent atau Normal
    if average_score > threshold:
        category = "Excellent"
    else:
        category = "Normal"
        
    return {
        'average_score': round(average_score, 2),
        'gender': data.gender,
        'performance': category
    }
