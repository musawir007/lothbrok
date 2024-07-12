
import requests
import random
import string
import json
import csv
import hashlib
from faker import Faker
import time

def tao_pass(kich_thuoc):
    chu_cai_so = string.ascii_letters + string.digits
    return ''.join(random.choice(chu_cai_so) for i in range(kich_thuoc))

def lay_mail():
    url = "https://api.mail.tm/domains"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()['hydra:member']
        else:
            print("Error when getting list of mail domains:")
            print(response.text)
            return None
    except Exception as e:
        print("Error! An error occurred. Please try again later:", e)
        return None

def tao_mail():
    fake = Faker()
    ten_mien_email = lay_mail()
    if ten_mien_email:
        ten_mien = random.choice(ten_mien_email)['domain']
        ten_nguoi_dung = tao_pass(10)
        mat_khau = 'Kh@ng270308'
        # mat_khau = 'bhutto786'
        sinh_nhat = fake.date_of_birth(minimum_age=18, maximum_age=45)
        ho = fake.first_name()
        ten = fake.last_name()
        url = "https://api.mail.tm/accounts"
        headers = {"Content-Type": "application/json"}
        du_lieu = {"address": f"{ten_nguoi_dung}@{ten_mien}", "password": mat_khau}
        
        try:
            response = requests.post(url, headers=headers, json=du_lieu)
            if response.status_code == 201:
                print("Successfully created email account")
                return f"{ten_nguoi_dung}@{ten_mien}", mat_khau, ho, ten, sinh_nhat
            else:
                print("Error when creating email account:")
                print(response.text)
                return None, None, None, None, None
        except Exception as e:
            print("Error! An error occurred. Please try again later:", e)
            return None, None, None, None, None

def tao_tk_fb(email, password, first_name, last_name, birthday):
    api_key = '882a8490361da98702bf97a021ddc14d'
    # api_key = '237759909591655|0f140aabedfb65ac27a739ed1a2263b1'
    secret = '62f8ce9f74b12f84c123cc23437a4a32'
    gender = random.choice(['M', 'F'])

    req = {
        'api_key': api_key,
        'attempt_login': True,
        'birthday': birthday.strftime('%Y-%m-%d'),
        'client_country_code': 'EN',
        'fb_api_caller_class': 'com.facebook.registration.protocol.RegisterAccountMethod',
        'fb_api_req_friendly_name': 'registerAccount',
        'firstname': first_name,
        'format': 'json',
        'gender': gender,
        'lastname': last_name,
        'email': email,
        'locale': 'en_US',
        'method': 'user.register',
        'password': password,
        'reg_instance': tao_pass(32),
        'return_multiple_errors': True
    }
    sorted_req = sorted(req.items(), key=lambda x: x[0])
    sig = ''.join(f'{k}={v}' for k, v in sorted_req)
    ensig = hashlib.md5((sig + secret).encode()).hexdigest()
    req['sig'] = ensig
    api_url = 'https://b-api.facebook.com/method/user.register'

    reg = goi_api(api_url, req)
    # Print the registration response for debugging
    print("Facebook registration response:", reg['session_info']['uid'])
    with open("successfully.csv", 'a', newline='') as file:
        writer = csv.writer(file)
        print("save the email")
        writer.writerows([[reg['session_info']['uid']]])
    
    # Save the response as a JSON file
    # with open(f"{'all/'}{email}.json", "w") as file:
    #     json.dump(reg, file, indent=4)

def goi_api(url, params, post=True):
    headers = {
        'User-Agent': '[FBAN/FB4A;FBAV/35.0.0.48.273;FBDM/{density=1.33125,width=800,height=1205};FBLC/en_US;FBCR/;FBPN/com.facebook.katana;FBDV/Nexus 7;FBSV/4.1.1;FBBK/0;]'
    }
    try:
        if post:
            response = requests.post(url, data=params, headers=headers)
        else:
            response = requests.get(url, params=params, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except Exception as err:
        print(f"Other error occurred: {err}")
    return {}

if __name__ == "__main__":
    so_luong_tk = int(input("Enter the number of accounts you want to create: "))
    for _ in range(so_luong_tk):
        email, password, first_name, last_name, birthday = tao_mail()
        if email and password and first_name and last_name and birthday:
            tao_tk_fb(email, password, first_name, last_name, birthday)
            time.sleep(random.uniform(1, 3))
