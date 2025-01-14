import uiautomator2 as u2
import time
serial = "d607681e"
# serial = "d607681e"
try:
    print(f"Connecting to device: {serial}")
    device = u2.connect("d607681e")
    print("Device connected successfully.")
    
except Exception as e:
    print(f"Error connecting to device: {e}")
    
def text_click(txt,tm):
    print(f"click {txt}")
    time.sleep(1)
    device(text=txt).wait(timeout=tm)
    device(text=txt).click()

def id_txt(txt,tm):
    print(f"click {txt}")
    time.sleep(1)
    device(resourceId=txt).wait(timeout=tm)
    device(resourceId=txt).click()

def dec_click(txt,tm):
    print(f"click {txt}")
    
    device(description=txt).wait(timeout=tm)
    device(description=txt).click()
