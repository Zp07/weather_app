from fastapi import FastAPI
from app.routes import router as weather_router

#Instancia de FastAPI con titulo y versión
app = FastAPI(title="Weather app",version="1.0")

#Incluir rutas de la API
app.include_router(weather_router)

@app.get("/")
def root():
    return {"message": "API funcionando correctamente"}

