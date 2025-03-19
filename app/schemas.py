from pydantic import BaseModel
from datetime import datetime

#Esquema para la creación de datos meteorológicos
class WeatherCreate(BaseModel):
    city: str
    tempeprature: float
    humidity: int
    condition: str

#Esquema de respuesta que extiende de su padre
class WeatherResponse(WeatherCreate):
    #Nuevas propiedades
    id: int
    recorded_at_: datetime
    class config:
        orm_mode:True