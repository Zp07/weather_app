from pydantic import BaseModel
from datetime import datetime

#Esquema de respuesta que extiende de su padre
class WeatherResponse():
    #Nuevas propiedades
    id: int
    recorded_at: datetime
    class Config:
        from_attributes = True