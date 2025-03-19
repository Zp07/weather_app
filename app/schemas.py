from pydantic import BaseModel
from datetime import datetime

#Esquema para la creación de datos meteorológicos
class WeatherCreate(BaseModel):
    city: str
    temperature: float
    humidity: int
    condition: str

#Esquema de respuesta que extiende de su padre
class WeatherResponse(WeatherCreate):
    #Nuevas propiedades
    id: int
    recorded_at: datetime
    class Config:
        from_attributes = True