import requests

user_name = "natas13"
password = "jmLTY0qiPZBbaKc9341cqPQZBJv7MQbY"

url = f"http://{user_name}.natas.labs.overthewire.org"

session = requests.Session()


response = session.get(url, auth = (user_name, password))
#response = session.post(url, auth = (user_name, password))


content = response.text


print(content)