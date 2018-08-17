import requests

user_name = "natas11"
password = "U82q5TCMMQ9xuFoI3dYX61s7OZD9JKoK"

url = f"http://{user_name}.natas.labs.overthewire.org"

session = requests.Session()

cookies = {"data" : "ClVLIh4ASCsCBE8lAxMacFMOXTlTWxooFhRXJh4FGnBTVF4sFxFeLFMK"}

#response = session.get(url, auth = (user_name, password))
response = session.post(url, auth =  (user_name, password), cookies = cookies)

content = response.text


print(content)