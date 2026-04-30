from fastapi import FastAPI
import json

app = FastAPI()

# მონაცემების ბაზის ჩატვირთვა
try:
with open('medical_data.json', 'r', encoding='utf-8') as f:
medical_db = json.load(f)
except Exception:
medical_db = {}

@app.get("/")
async def root():
return {"message": "DOGMEAL System is Online"}

@app.get("/search_symptom/{query}")
async def search(query: str, lang: str = "ka"):
result = medical_db.get(lang, {}).get(query, "ინფორმაცია ვერ მოიძებნა.")
return {"response": result}



