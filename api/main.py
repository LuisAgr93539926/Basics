import requests

request = requests.get("https://tokog44785.pythonanywhere.com/")
data = request.json()

print(data)
