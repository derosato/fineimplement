from fastapi import FastAPI
from app.jokes import get_random_joke

app = FastAPI(title="Random Joke API")

@app.get("/joke")
def read_joke():
    return {"joke": get_random_joke()}

@app.get("/")
def root():
    return {"message": "Welcome to the Random Joke API! Go to /joke for a joke."}
