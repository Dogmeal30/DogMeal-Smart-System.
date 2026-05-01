from flask import Flask, jsonify, render_template, request
import json
import os

app = Flask(__name__)

class DogMealEngine:
    def __init__(self):
        self.theme = "Dark_Grey_Green_Accent"
        self.data_path = 'dogmeal_encyclopedia.json'
        self.sos_path = 'sos_recovery' # ჩვენი SOS ფაილის სახელი
        
    def get_breed_info(self, breed_name):
        try:
            if os.path.exists(self.data_path):
                with open(self.data_path, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    return data.get(breed_name, None)
            return None
        except:
            return None

    def get_sos_data(self):
        try:
            if os.path.exists(self.sos_path):
                with open(self.sos_path, 'r', encoding='utf-8') as f:
                    return json.load(f)
            return {"error": "SOS მონაცემები ვერ მოიძებნა"}
        except:
            return {"error": "ფაილის წაკითხვის შეცდომა"}

engine = DogMealEngine()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/breed/<name>')
def get_breed(name):
    info = engine.get_breed_info(name)
    if info:
        return jsonify(info)
    return jsonify({"error": "Breed not found"}), 404

@app.route('/sos')
def sos_info():
    # ეს ფუნქცია პასუხისმგებელია SOS ღილაკზე
    data = engine.get_sos_data()
    return jsonify(data)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=10000)
