from pydantic import BaseModel
from datetime import datetime
class WeatherCreate(BaseModel):
    city: str
    tempeprature: float
    humidity: int
    condition: str

class WeatherResponse(WeatherCreate):
    id: int
    recorded_at_: datetime
    class config:
        from_atributes:True