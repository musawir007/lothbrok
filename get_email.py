import requests
import sys
import time
import os
import http.client
os.system("clear")

print("\033[92m")

print(''' _ __ ___  _   _ ___  __ ___      _(_)_ __
| '_ ` _ \| | | / __|/ _` \ \ /\ / / | '__|
| | | | | | |_| \__ \ (_| |\ V  V /| | |
|_| |_| |_|\__,_|___/\__,_| \_/\_/ |_|_|''')



def slow_print(text, delay=0.1, color='\033[92m'):
    # \033[92m is the ANSI escape code for green text
    reset = '\033[0m'  # ANSI escape code to reset color
    for char in text:
        sys.stdout.write(f"{color}{char}{reset}")
        sys.stdout.flush()
        time.sleep(delay)
    print()  # Move to the next line

# Example usage
slow_print("__________________________________________________", delay=0.02)
print("\033[92m")

slow_print("<<<<<<<<<<<<<<<<<<<< GENERATE EMAIL >>>>>>>>>>>>>>", delay=0.02)

print("\033[92m")
slow_print("__________________________________________________", delay=0.02)
print("\033[92m")









url = "https://temp-mail-temporary-email.p.rapidapi.com/domain"

payload = "-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"count\"\r\n\r\n1\r\n-----011000010111000001101001--\r\n\r\n"
headers = {
	"x-rapidapi-key": "b6d2c5b5d9msh03f41a2ef871027p11a1e8jsn797fd7bafe37",
	"x-rapidapi-host": "temp-mail-temporary-email.p.rapidapi.com",
	"Content-Type": "multipart/form-data; boundary=---011000010111000001101001"
}

response = requests.post(url, data=payload, headers=headers)



slow_print("**************************************************", delay=0.02)
print("\033[92m")
print(f"email: {response.json()[0]}")
mail_box = response.json()[0]
print("\033[92m")
slow_print("**************************************************", delay=0.02)



while True:
    new = input("get sms yes or not :- ")

    if new.lower() == "yes":
        conn = http.client.HTTPSConnection("temp-mail-temporary-email.p.rapidapi.com")
        
        payload = f"-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"email\"\r\n\r\n{mail_box}\r\n-----011000010111000001101001--\r\n\r\n"

        headers = {
            'x-rapidapi-key': "b6d2c5b5d9msh03f41a2ef871027p11a1e8jsn797fd7bafe37",
            'x-rapidapi-host': "temp-mail-temporary-email.p.rapidapi.com",
            'Content-Type': "multipart/form-data; boundary=---011000010111000001101001"
        }

        conn.request("POST", "/get_messages", payload, headers)

        res = conn.getresponse()
        data = res.read()

        print(data.decode("utf-8"))
    pr = input("tool exit :- ")

    if pr.lower() == 'exit':
        break

