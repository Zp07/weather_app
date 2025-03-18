from sqlalchemy import Column,Integer,String,Float,DateTime
from app.database import Base
from datetime import datetime

class WeatherData(Base):
    __tablename__ = "Weather app"
    id = Column(Integer, primary_key=True, index=True)
    city = Column(String, index=True)
    temperature = Column(Float)
    humidity = Column(Integer)
    condition = Column(String)
    recorded_at = Column(DateTime, default=datetime.utcnow)