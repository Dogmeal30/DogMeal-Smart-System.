import json

class DogMealEngine:
def __init__(self):
# ბრენდის ფერების და ლოგოს პოზიციონირების პარამეტრები
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
return "თქვენს ძაღლს მეტი დასვენება სჭირდება ოპტიმალური განვითარებისთვის."
return "ძილის რეჟიმი ნორმაშია."

def health_check(self, symptoms):
"""ჯანმრთელობის სიმპტომების კონტროლი"""
alerts = {
"Lethargy": "დაბალი ენერგია - დააკვირდით კვებას.",
"Appetite Loss": "მადის დაკარგვა - რეკომენდირებულია ვეტერინართან ვიზიტი.",
"Coughing": "ხველება - შეამოწმეთ გულის ან ფილტვების მდგომარეობა."
}
found_issues = [alerts[s] for s in symptoms if s in alerts]
return found_issues if found_issues else ["სიმპტომები არ ფიქსირდება."]

# ინიციალიზაცია
engine = DogMealEngine()




