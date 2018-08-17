import requests

user_name = "natas4"
password = "Z9tkRkWmpt9Qr7XrR5jWRkgOU901swEZ"

url = f"http://{user_name}.natas.labs.overthewire.org"

headers = {"referer" : "http://natas5.natas.labs.overthewire.org/"}

response = requests.get(url, auth = (user_name, password), headers = headers)
content = response.text

print(content)
