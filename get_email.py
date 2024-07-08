import requests
from termcolor import colored
import sys
import time
import os
# os.system("pip install pyfiglet")

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
slow_print("______________________________________________________", delay=0.05)
print("\033[92m")

slow_print("<<<<<<<<<<<<<<<<<<<< GENERATE EMAIL >>>>>>>>>>>>>>>>>>>", delay=0.05)

print("\033[92m")
slow_print("______________________________________________________", delay=0.05)
print("\033[92m")







url = "https://temp-mail-temporary-email.p.rapidapi.com/domain"

payload = "-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"count\"\r\n\r\n1\r\n-----011000010111000001101001--\r\n\r\n"
headers = {
	"x-rapidapi-key": "d97ad460d8msh47ea613332686f8p10fe95jsn7de0ccd346bb",
	"x-rapidapi-host": "temp-mail-temporary-email.p.rapidapi.com",
	"Content-Type": "multipart/form-data; boundary=---011000010111000001101001"
}

response = requests.post(url, data=payload, headers=headers)

slow_print("*******************************************************", delay=0.05)
print("\033[92m")
print(f"email: {response.json()[0]}")
print("\033[92m")
slow_print("*******************************************************", delay=0.05)
