from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import WeatherData
from app.schemas import WeatherCreate, WeatherResponse

router = APIRouter()

#Ruta para traer todos los registros
@router.get("/weather/", response_model=list[WeatherResponse])
def get_all_weather(db: Session = Depends(get_db)):
    return db.query(WeatherData).all()

#Ruta para agregar un nuevo registro del clima
@router.post("/weather/", response_model=WeatherResponse)
def create_weather(data: WeatherCreate, db: Session = Depends(get_db)):
    new_weather = WeatherData(**data.dict())
    db.add(new_weather)
    db.commit()
    db.refresh(new_weather)
    return new_weather