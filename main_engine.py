from flask import Flask, jsonify, render_template, request
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
                    return data.get(breed_name, None)
            return None
        except Exception as e:
            return None

engine = DogMealEngine()

@app.route('/')
def home():
    # ეს ხაზი ეუბნება სერვერს, რომ templates/index.html აჩვენოს
    return render_template('index.html')

@app.route('/breed/<name>')
def get_breed(name):
    info = engine.get_breed_info(name)
    if info:
        return jsonify(info)
    return jsonify({"error": "Breed not found"}), 404

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=10000)




