from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import WeatherData
from app.schemas import WeatherCreate, WeatherResponse
from app.services.weather_api import get_weather_city

router = APIRouter()

#Ruta para traer todos los registros
@router.get("/weather/", response_model=list[WeatherResponse])
def get_all_weather(db: Session = Depends(get_db)):
    return db.query(WeatherData).all()

#Ruta obtener datos del clima en tiempo real 
@router.get("/weather/{city}")
def get_weather_api(city: str):
    weather_data = get_weather_city(city)
    if weather_data:
        return weather_data
    else:
        raise HTTPException(status_code=404, detail="City not found")
    
#Ruta para agregar un nuevo registro del clima
@router.post("/weather/", response_model=WeatherResponse)
def create_weather(data: WeatherCreate, db: Session = Depends(get_db)):
    new_weather = WeatherData(**data.dict())
    db.add(new_weather)
    db.commit()
    db.refresh(new_weather)
    return new_weather