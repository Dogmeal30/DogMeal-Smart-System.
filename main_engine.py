from fastapi import FastAPI, HTTPException
import json

app = FastAPI(title="DOGMEAL Smart System API")

# მონაცემების ჩატვირთვა ჩვენი ფაილებიდან
def load_data(file_name):
with open(file_name, 'r', encoding='utf-8') as f:
return json.load(f)

@app.get("/")
async def root():
return {"message": "DOGMEAL სისტემა აქტიურია და მზად არის მუშაობისთვის!"}

@app.get("/check-travel/{country}")
async def check_travel(country: str):
data = load_data('travel_standards.json')
return data['standards'].get(country.upper(), "ინფორმაცია ამ ქვეყანაზე მალე დაემატება.")

@app.get("/get-symptom/{lang}/{query}")
async def get_symptom(lang: str, query: str):
data = load_data('dogmeal_encyclopedia.json')
result = data['encyclopedia'].get(lang, {}).get('symptoms', {}).get(query)
return {"recommendation": result or "გთხოვთ, მიმართოთ ვეტერინარს ზუსტი დიაგნოზისთვის."}

@app.post("/activate-sos/{pet_id}")
async def activate_sos(pet_id: str):
# აქედან იგზავნება შეტყობინება პატრონთან
return {"status": "SOS რეჟიმი ჩაირთო!", "pet_id": pet_id}
