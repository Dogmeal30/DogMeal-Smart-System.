from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
return {"status": "DOGMEAL Online", "message": "სისტემა მზად არის!"}

@app.get("/test")
def test():
return {"health": "ok"}

