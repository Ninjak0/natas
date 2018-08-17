import requests
import base64
import binascii

coded_pass = "3d3d516343746d4d6d6c315669563362"
pass_hex = binascii.unhexlify(coded_pass)
pass_reverted = pass_hex[::-1]
pass_base64 = base64.b64decode(pass_reverted)

user_name = "natas8"
password = "DBfUBfqQG69KvJvJ1iAbMoIpwSNQ9bWe"

url = f"http://{user_name}.natas.labs.overthewire.org"

session = requests.Session()

#response = session.get(url + "/index-source.html", auth = (user_name, password))
response = session.post(url, data= {"secret" : pass_base64, "submit" : "submit"}, auth =  (user_name, password))

content = response.text

print(content)



