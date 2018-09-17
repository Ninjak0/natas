import requests
import string

characters = string.ascii_lowercase + string.ascii_uppercase + string.digits

user_name = "natas16"
password = "WaIHEacj63wnNIBROHeqi3p9t0m5nhmh"

url = f"http://{user_name}.natas.labs.overthewire.org"

session = requests.Session()


response = session.get(url, auth = (user_name, password))

content = response.text


print(content)