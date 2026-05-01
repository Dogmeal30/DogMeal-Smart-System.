from flask import Flask
import json

app = Flask(__name__)

class DogMealEngine:
    def __init__(self):
        self.theme = "Dark_Grey_Green_Accent"
        
    def calculate_nutrition(self, breed, weight):
        base_calories = weight * 30 + 70
        return f"კალორიები {breed}-სთვის: {int(base_calories)} კკალ."

# ვქმნით მთავარ გვერდს, რომ Render-მა დაინახოს მუშაობა
@app.route('/')
def home():
    engine = DogMealEngine()
    result = engine.calculate_nutrition("Labrador", 30)
    return f"<h1>DogMeal Pro System is Online!</h1><p>{result}</p>"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=10000)




