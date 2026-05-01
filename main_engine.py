from flask import Flask, jsonify
import json
import os

app = Flask(__name__)

class DogMealEngine:
    def __init__(self):
        self.theme = "Dark_Grey_Green_Accent"
        self.data_path = 'dogmeal_encyclopedia.json'

    def get_breed_info(self, breed_name):
        """ენციკლოპედიიდან ჯიშის მონაცემების ამოღება"""
        try:
            if os.path.exists(self.data_path):
                with open(self.data_path, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    # ვეძებთ კონკრეტულ ჯიშს ბაზაში
                    breed_data = data.get(breed_name)
                    if breed_data:
                        return breed_data
            return None
        except Exception as e:
            return f"შეცდომა მონაცემების წაკითხვისას: {e}"

    def calculate_daily_intake(self, weight, activity_multiplier=1.2):
        """კალორიების გამოთვლის ზოგადი ფორმულა"""
        return int((weight * 30 + 70) * activity_multiplier)

# მთავარი გვერდი (Dashboard)
@app.route('/')
def home():
    engine = DogMealEngine()
    # სატესტოდ ამოვიღოთ ინფორმაცია (მაგალითად "German Shepherd")
    # შენი JSON-ის მიხედვით აქ ჩაწერე ის სახელი, რაც ფაილში გაქვს
    breed = "German Shepherd" 
    info = engine.get_breed_info(breed)
    
    if info:
        calories = engine.calculate_daily_intake(35) # 35 კგ სატესტოდ
        return f"""
        <body style="background-color: #1a1a1a; color: #2ecc71; font-family: sans-serif; padding: 50px;">
            <h1>DogMeal Pro: {breed}</h1>
            <p style="color: #ffffff;">რეკომენდირებული კალორია: {calories} კკალ</p>
            <div style="border: 1px solid #2ecc71; padding: 20px;">
                <h3>ინფორმაცია ენციკლოპედიიდან:</h3>
                <pre style="color: #bdc3c7;">{json.dumps(info, indent=4, ensure_ascii=False)}</pre>
            </div>
        </body>
        """
    else:
        return "<h1>სისტემა ჩართულია, მაგრამ ბაზაში ეს ჯიში ვერ მოიძებნა.</h1>"

if __name__ == "__main__":
    # Render-ისთვის პორტის მითითება
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)




