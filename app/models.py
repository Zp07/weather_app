from sqlalchemy import Column,Integer,String,Float,DateTime
from app.database import Base
from datetime import datetime

#Modelo de la tabla de datos
class WeatherData(Base):
    #Nombre de la base de datos
    __tablename__ = "Weather_app"

    #Propiedades
    id = Column(Integer, primary_key=True, index=True)
    city = Column(String, index=True)
    temperature = Column(Float)
    humidity = Column(Integer)
    condition = Column(String)
    recorded_at = Column(DateTime, default=datetime.utcnow)