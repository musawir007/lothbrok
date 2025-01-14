import uiautomator2 as u2
import cv2
import numpy as np
from time import sleep

def show_mobile_screen():
    # Connect to the mobile device
    device = u2.connect("d607681e")  # Replace with device IP or serial if not using default
    
    print(f"Connected to device: {device.device_info['model']}")

    while True:
        # Take a screenshot from the device
        screenshot = device.screenshot(format='opencv')  # Get image as a NumPy array
        
        if screenshot is not None:
            # Resize the image to 720x1280 pixels
            resized_screenshot = cv2.resize(screenshot, (400, 600))
            # Display the resized image using OpenCV
            cv2.imshow("musawir mobile", resized_screenshot)
        else:
            print("Failed to get screenshot")

        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        # sleep(1)  # To control the refresh rate
    
    # Close the OpenCV window
    cv2.destroyAllWindows()

# if __name__ == "__main__":
show_mobile_screen()
