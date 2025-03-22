from pydantic import BaseModel
from datetime import datetime

#Esquema de respuesta que extiende de su padre
class WeatherResponse(BaseModel):
    #Propiedades de ubicación
    id: int
    city: str
    region: str
    country: str
    latitude: float
    longitude: float
    timezone: str

    #Propiedades del clima
    temperature : float
    humidity : int
    condition : str
    wind_speed : float
    wind_direction : str
    pressure : float
    precitipation : float
    cloud_cover : int
    feels_like : float
    dew_point : float
    visibility : float
    uv_index : int
    gus_speed : float
    
    #Propiedad de fecha de registro
    recorded_at: datetime
    
    #Configuración de Pydantic
    class Config:
        from_attributes = True