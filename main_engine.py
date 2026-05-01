import json

class DogMealEngine:
    def __init__(self):
        # ბრენდის ფერების და ლოგოს პარამეტრები
        self.theme = "Dark_Grey_Green_Accent"
        self.logo_position = "Center"
        
    def calculate_nutrition(self, breed, weight, age, activity_level):
        """კვების დღიური: ულუფების გამოთვლა"""
        base_calories = weight * 30 + 70
        if activity_level == "High":
            base_calories *= 1.5
        return f"რეკომენდირებული დღიური ნორმა {breed}-სთვის: {int(base_calories)} კკალ."

    def sleep_monitor(self, age_months, sleep_hours):
        """ძილის რეჟიმის კონტროლი"""
        required_sleep = 18 if age_months < 6 else 14
        if sleep_hours < required_sleep:
            return "თქვენს ძაღლს მეტი დასვენება სჭირდება."
        return "ძილის რეჟიმი ნორმაშია."

# აპლიკაციის ობიექტი სერვერისთვის (Render ამას ეძებს)
app = DogMealEngine()




