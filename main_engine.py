from fastapi import FastAPI
import json
import random

app = FastAPI(title="DOGMEAL Global Hub")

# ყველა მონაცემის ჩატვირთვა
def get_db(file):
with open(file, 'r', encoding='utf-8') as f:
return json.load(f)

@app.get("/")
async def status():
return {"status": "DOGMEAL Online", "version": "1.0.2", "owner": "Begheli"}

# კვების კალკულატორი
@app.get("/calc-feed")
async def calc(weight: float, activity: int):
# ფორმულა: წონა * 25გრ + აქტივობის კოეფიციენტი
portion = (weight * 25) * (1 + (activity * 0.1))
return {"portion_grams": round(portion, 0), "message": "DOGMEAL-ის ოპტიმალური დოზა"}

# ინტელექტუალური სიმპტომების ძებნა
@app.get("/check-symptom/{query}")
async def check(query: str):
db = get_db('dogmeal_intelligence.json')
result = db['symptoms_catalog'].get(query, "ინფორმაცია ვერ მოიძებნა. დაუკავშირდით ვეტერინარს.")
return {"info": result}

# სახალისო ფოტო-მესიჯის გენერატორი
@app.get("/daily-fun")
async def fun():
messages = [
"ნახე, როგორ ველოდები შენს მოსვლას! 🐾",
"დღეს ძალიან კარგი ბიჭი ვიყავი! 🦴",
"უკვე ჭამის დროა, არ დაგავიწყდეს! 🍽️"
]
return {"message": random.choice(messages)}


