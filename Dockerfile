#Imagen inicial base
FROM python:3.13.2

#Establecer directorio inicial
WORKDIR /app

#Copiar las dependencias
COPY . .

#Instalar dependencias
RUN pip install --no-cache-dir -r requirements.txt

#Comando iniciar app
CMD [ "uvicorn","app.main:app","--host","0.0.0.0","--port","8000" ]