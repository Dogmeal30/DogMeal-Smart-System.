# DOGMEAL Smart Feeding & Fun Module

def calculate_portion(weight, activity_level, age_months):
"""
ითვლის საკვების ზუსტ დოზას:
- weight: წონა (კგ)
- activity_level: აქტივობა (1-5)
- age_months: ასაკი თვეებში
"""
base_portion = weight * 25 # საბაზისო ფორმულა
if age_months < 12: base_portion *= 1.5 # ლეკვებს მეტი სჭირდებათ

final_portion = base_portion * (1 + (activity_level * 0.1))
return round(final_portion, 2)

def get_fun_photo_message():
# სახალისო შეტყობინებები, რომლებიც ფოტოებთან ერთად მივა პატრონთან
messages = [
"ნახე, როგორ ველოდები შენს მოსვლას! 🐾",
"დღეს ძალიან კარგი ბიჭი ვიყავი, დამატებითი სასუსნავი ხომ არ მეკუთვნის? 🦴",
"უკვე ჭამის დროა, არ დაგავიწყდეს! 🍽️",
"უბრალოდ მინდოდა მეთქვა, რომ საუკეთესო პატრონი ხარ! ❤️"
]
import random
return random.choice(messages)
