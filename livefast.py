
from fastapi import FastAPI

app = FastAPI()

@app.get("/hello")
async def hello():
    return "Hello World"

@app.get("/hello/{name}")
async def hello(name:str):
    return f"Hey {name}, how are you??"


indian_places = {
    "Hyderabad":['Charminar','Golkonda','Falaknama palace'],
    "Mumbai":['Gateway of India','Elepahant caves'],
    "Delhi":['Red fort','Qutub minar','India gate']
}

@app.get("/get_places/{places}")
async def get_places(places):
    return indian_places.get(places)  ## type docs after hhtps url to get web 
