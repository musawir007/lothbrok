import uiautomator2 as u2
import time
from clicking import *
from faker import Faker
import random
import threading
import csv
fake = Faker()
from setting import *
phone_number = f"0348{fake.random_number(digits=7):07d}"
# Initialize Faker instance
with open('name.csv', 'r', newline='') as file:
    reader = csv.DictReader(file)
    rows = list(reader)


def connect_device(serial):
    """
    Function to connect to an Android device.
    :param serial: The serial number of the device.
    :return: u2 device object if successful, None otherwise.
    """
    try:

        print(f"Connecting to device: {serial}")
        device = u2.connect("d607681e")
        print("Device connected successfully.")
        return device
    except Exception as e:
        print(f"Error connecting to device: {e}")
        return None

def open_app(device, package_name, activity_name=None):
    
    try:
        """
        Function to launch an app on the connected Android device.
        :param device: The u2 device object.
        :param package_name: The package name of the app to be launched.
        :param activity_name: The specific activity of the app (optional).
        """
        try:
            
            if activity_name:
                print(f"Launching app with package: {package_name}, activity: {activity_name}")
                device.shell(f"pm clear {package_name}")
                time.sleep(4)
                print("app data clear")
                
                device.app_start(package_name, activity=activity_name)
            
                # time.sleep(2)
                # print("click allow")
                # try:
                #     device(text="ALLOW").click()
                # except:
                #     pass
                # # 

                
            
                # text_click("START",10)
                

                # time.sleep(1)
            
                # text_click("Messenger(1)",10)
                # # text_click("Messenger(1)",10)
                # time.sleep(1)
                # text_click("CLONE",10)
                # # time.sleep(2)
                # # id_txt("com.dualspace.multispace.android:id/iv_add",10)
                # # text_click("Facebook(2)",10)
                # # text_click("CLONE",10)
                # # time.sleep(3)
                # # text_click("Messenger(2)",10)
                # text_click("Messenger(1)",10)
                # try:
                
                # time.sleep(10)

                # time.sleep(2)
                # print("click allow")
                # try:
                #      device(text="ALLOW").click()
                # except:
                #     pass
                # # 

                
            
                text_click("START",10)
                

                # time.sleep(1)
                if facebook == 1:
                    
                    text_click("Facebook(1)",10)
                    time.sleep(1)
                    text_click("CLONE",10)
                    
                    text_click("Facebook(1)",10)
                if messanger == 1:
                    text_click("Messenger(1)",10)
                    time.sleep(1)
                    text_click("CLONE",10)
                    text_click("Messenger(1)",10)
                if lite ==1:
                    text_click("Lite(1)",10)
                    time.sleep(1)
                    text_click("CLONE",10)
                    text_click("Lite(1)",10)
                # text_click("Messenger(1)",10)
                # try:
                #     device(text="Choose an account").wait(20)
                # except:
                #     pass
                # id_txt("com.google.android.gms:id/cancel",120)
                
                # time.sleep(1)
                for i in range(5):
                    try:
                        try:
                            text_click("Create new account",10)
                        except:
                            try:
                                if messanger == 1:
                                    text_click("Messenger(1)",1)
                                    text_click("Create new account",1)
                                    
                                if facebook == 1:
                                    text_click("Facebook(1)",1)
                                    text_click("Create new account",1)
                            except:
                                pass
                    except:
                        p
                    else:
                        break
                # except:
                    # text_click("Messenger(1)",10)
                    # text_click("Create new account",30)
                # try:
                #     text_click("Next",1)
                # except:
                #     pass
                
                    
                text_click("Get started",60)
                
                    
                time.sleep(2)
                if facebook == 1:
                    try:
                        text_click("ALLOW",10)
                    except:
                        pass
                text_click("First name",60)  # Focus on the first name field
                if rows:
                    # Randomly select a row
                    random_row = random.choice(rows)
                    
                    device(focused=True).set_text(random_row['fname'])
                    print(f"first name : {random_row['fname']}")
                    time.sleep(1)
                    
                    text_click("Last name",60)  # Focus on the first name field
                    device(focused=True).set_text(random_row['lname'])
                    print(f"last name : {random_row['lname']}")

                    # Remove the selected row
                    rows.remove(random_row)

                    # Write the updated rows back to the CSV file
                    with open('name.csv', 'w', newline='') as file:
                        # Create a DictWriter object using the same fieldnames
                        writer = csv.DictWriter(file, fieldnames=reader.fieldnames)
                        
                        # Write the header row
                        writer.writeheader()
                        
                        # Write the remaining rows
                        writer.writerows(rows)
                else:
                    print("The file is empty or no rows found.")
                
                
                # time.sleep(1)
                text_click("Next",60)
                # time.sleep(1)
                text_click("SET",70)
                # time.sleep(1)
                text_click("Next",60)
                time.sleep(1)
                text_click("Next",60)
                listt = ["18","19","20","21","22","23","24","25","26"]
                rnd = random.choice(listt)
                device(focused=True).set_text(rnd)
                # time.sleep(1)
                text_click("Next",60)
                # time.sleep(1)
                text_click("OK",60)
                # time.sleep(1)
                text_click("Female",60)
                # time.sleep(1)
                text_click("Next",60)
                # time.sleep(1)
                text_click("Mobile number",60)
                device(focused=True).set_text(phone_number)

                # time.sleep(1)
                text_click("Next",60)
                try:
                    text_click("Continue creating account",1)
                except:
                    pass
                # time.sleep(2)
                device(focused=True).set_text("bhutto786")
                # time.sleep(1)
                text_click("Next",60)
                # time.sleep(2)
                text_click("Not now",60)
                # time.sleep(2)
                text_click("I agree",10)
                # time.sleep(5)
                try:
                    text_click("Continue",6)
                except:
                    pass
                # try:
                #     text_click("No, create new account",3)
                # except:
                #     pass
                # try:
                #     text_click("Not now",2)
                # except:
                #     pass
                # else:
                #     p
                text_click("I didn’t get the code",70)
                
                # time.sleep(2)
                text_click("Confirm by email",60)
                # time.sleep(4)
                text_click("Email",60)
                time.sleep(3)
                if io_tempmail == 1:
                    device.app_start("io.tempmail.android", activity="io.tempmail.mvp.root.RootActivity")
                    while True:
                        try:
                            dec_click("My Emails",5)
                            text_click("DELETE",2)
                        except:
                            pass
                        else:
                            break
                    # time.sleep(10)
                    #device.app_clear("io.tempmail.android")
                    device.app_start("io.tempmail.android", activity="io.tempmail.mvp.root.RootActivity")
                    dec_click("Mailbox",5)
                    text_click("REFRESH",10)
                    time.sleep(1)
                    dec_click("My Emails",5)
                    global emmail
                    # emmail = ""
                    while True:
                        try:
                            text_click("COPY",1)
                            
                            element = element = device(resourceId="io.tempmail.android:id/emailTxt")
                            emmail =  element.get_text()
                            print(emmail)
                        except:
                            pass
                        else:
                            break
                    # time.sleep(1)
                    try:
                        device.press('recent')
                        device.press('recent')
                    except:
                        print("any error")
                        
                    # time.sleep(2)
                    paste_field = device(focused=True)
                    paste_field.long_click()
                    # time.sleep(2)
                    text_click("Paste",10)
                    # time.sleep(2)
                    text_click("Next",10)
                    # time.sleep(10)
                    device(text="Enter the confirmation code").wait(timeout=60)
                    #device.app_clear("io.tempmail.android")
                    # time.sleep(2)
                    device.app_start("io.tempmail.android", activity="io.tempmail.mvp.root.RootActivity")
                    
                    dec_click("Mailbox",10)
                    # device(description="Mailbox").click()
                    
                    def email():
                        global numb
                        numb = 1
                        try:
                            while True:
                                if numb == 7:
                                    m
                                element = device(resourceId="io.tempmail.android:id/emailSubjectTV")
                                
                                # Check if the element exists
                                if element.exists:
                                    # Get the text of the element
                                    text = element.get_text()
                                    global vf
                                    print(f"email get code is : {text[:5]}")
                                    vf = text[:5]
                                    break
                                else:
                                    print("Element not found!")
                                    text_click("REFRESH",3)
                                    time.sleep(3)
                                numb +=1
                        except:
                            pass
                    email()
                if org_tempmail==1:
                    device.app_start("com.tempmail", activity="com.tempmail.splash.SplashActivity")
                    time.sleep(2)
                    try:
                        id_txt("com.tempmail:id/ivClose",5)
                    except:
                        pass
                    id_txt("com.tempmail:id/btnChange",10)
                    try:
                        text_click("YES",1)
                    except:
                        pass
                    time.sleep(5)
                    # global emmail
                    # emmail = ""
                    while True:
                        try:
                            id_txt("com.tempmail:id/btnCopy",10)
                            element = element = device(resourceId="com.tempmail:id/tvEmail")
                            emmail =  element.get_text()
                            print(emmail)
                        except:
                            pass
                        else:
                            break
                    time.sleep(1)
                    device.press('recent')
                    device.press('recent')
                    time.sleep(2)
                    paste_field = device(focused=True)
                    paste_field.long_click()
                    time.sleep(2)
                    text_click("Paste",10)
                    time.sleep(2)
                    text_click("Next",10)
                    time.sleep(1)
                    device.app_start("com.tempmail", activity="com.tempmail.splash.SplashActivity")
                    try:
                        id_txt("com.tempmail:id/ivClose",5)
                    except:
                        pass
                    try:
                        text_click("Continue to app",2)
                    except:
                        pass
                    text_click("Inbox",10)
                    time.sleep(1)
                    try:
                        while True:
                            # Find the element by resource ID
                            element = device(resourceId="com.tempmail:id/tvSubject")
                            
                            # Check if the element exists
                            if element.exists:
                                # Get the text of the element
                                text = element.get_text()
                                print(f"email get code is : {text[:5]}")
                                global vf
                                vf = text[:5]

                                break
                            else:
                                print("Element not found!")
                    except:
                        pass
                print("tab1")
                device.press('recent')
                print("tab2")
                device.press('recent')
                #device.app_clear("io.tempmail.android")
                time.sleep(3)
                while True:
                    try:
                        device(focused=True).set_text(vf)
                    except:
                        device.app_start("io.tempmail.android", activity="io.tempmail.mvp.root.RootActivity")
                    
                        dec_click("Mailbox",10)
                        email()
                        print("tab1")
                        device.press('recent')
                        print("tab2")
                        device.press('recent')
                    else:
                        break
                time.sleep(1)
                text_click("Next",10)
                time.sleep(1)
                try:
                    element =text_click("Add picture",60)
                    # time.sleep(1)
                    # device(text="Choose from Gallery").click()
                    # time.sleep(1)
                    # device(text="ALLOW").click()
                    # time.sleep(6)
                    # device(scrollable=True).scroll.to(description="images.jpeg, 4.60 kB, 3:15 AM")
                    # time.sleep(1)
                    # device(description="images.jpeg, 4.60 kB, 3:15 AM").click()
                    # time.sleep(1)
                    # device(text="Done").click()
                    # time.sleep(60)
                    time.sleep(1)
                    while True:
                        try:
                            print("account create successfully")
                            with open("create_idz.csv", 'a', newline='') as file:
                                writer = csv.writer(file)
                                print("save the email")
                                writer.writerows([[emmail]])
                        except:
                            
                            pass
                        else:
                            break
                    
                except:
                    pass
                    
                # time.sleep(3)
                # device(text="Choose from Gallery").click()
                # time.sleep(3)
                # device(text="ALLOW").click()
                # time.sleep(4)
                # device.swipe(500, 1000, 500, 500)





                # number_pickers = device(resourceId="android:id/numberpicker_input")
                # index = 2  
                # if number_pickers.exists:
                #     number_pickers[index].set_text("2000")  
                # else:
                #     print("Number picker not found!")
            

            else:
                print(f"Launching app with package: {package_name}")
                device.app_start(package_name)
            print("App launched successfully.")
        except Exception as e:
            print(f"Error launching app: {e}")
    except:
        pass
            # break
            
# Main program
if __name__ == "__main__":
    serial = "d607681e"  # Replace with your device's serial number
    # serial = "d607681e"  # Replace with your device's serial number
    # package_name = "com.dualspace.multispace.android"
    package_name = "com.dualspace.multispace.android"
    activity_name = "com.dualspace.multispace.ui.activity.SplashActivity" 
    # package_name = "com.dualspace.multispace.android"
    # activity_name = "com.dualspace.multispace.ui.activity.SplashActivity"  # Specify the activity if needed

    # Connect to the device
    device = connect_device(serial)

    if device:
        # Open the specified app
        open_app(device, package_name, activity_name)
    else:
        print("Failed to connect to the device.")

