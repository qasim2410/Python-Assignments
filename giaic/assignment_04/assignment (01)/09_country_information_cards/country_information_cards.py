import requests
response = requests.get("https://restcountries.com/v3.1/all")
print(response)

response = requests.get("https://restcountries.com/v3.1/all")

if response.status_code == 200:
    countries = response.json()
    print("data")
else:
    print("Error:", response.status_code)