from datetime import datetime
import requests

NUTRITIONIX_APP_ID = ""
NUTRITIONIX_API_KEY = ""

SHEETY_USERNAME = ""
SHEETTY_PROJECT_NAME = "'"
SHEET_NAME = ""

headers = {
    "x-app-id": NUTRITIONIX_APP_ID,
    "x-app-key": NUTRITIONIX_API_KEY,
}

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

nutrionsix_params = {
    "query": input("What exercise did you do?: "),
    "gender": "male",
    "weight_kg": 68,
    "height_cm": 170.5,
    "age": 20
}

response = requests.post(url=exercise_endpoint,
                         headers=headers,
                         json=nutrionsix_params)
response.raise_for_status()
my_result = response.json()


sheety_endpoint = f"https://api.sheety.co/{SHEETY_USERNAME}/{SHEETTY_PROJECT_NAME}/{SHEET_NAME}"

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in my_result["exercises"]:
    sheety_params = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"],
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

sheety_authorization = {
    "Authorization": "Bearer dsaasdasda32389oadhshe0qw01eh0nj01j0"}

sheety_response = requests.post(url=sheety_endpoint,
                                json=sheety_params,
                                headers=sheety_authorization)
print(sheety_response.text)
