import time
from tracemalloc import start
from ppadb.client import Client as AdbClient


client = AdbClient(host="127.0.0.1", port=5037) # Default is "127.0.0.1" and 5037
devices = client.devices()

device = devices[0]

print(f'Connected to {device}')
# number = "(480) 359-8707"

# Return Home
time.sleep(1)
device.shell("input touchscreen tap 540 2275")

# Close ALl Apps
time.sleep(1)
device.shell("input touchscreen tap 230 2275")
time.sleep(1)
device.shell("input touchscreen tap 540 1850")

# Click "PHONE"
time.sleep(1)
device.shell("input touchscreen tap 135 2067")

# Click "options"
time.sleep(1)
device.shell("input touchscreen tap 993 195")

# Click "settings"
time.sleep(1)
device.shell("input touchscreen tap 831 535")

# Click "blocked numbers"
time.sleep(1)
device.shell("input touchscreen tap 540 415")

# Click "Add phone number" input field
time.sleep(1)
device.shell("input touchscreen tap 540 550")

num_max = 6232649999
num_start = 6232641777
az_codes = [602, 520, 480, 623, 928]
while num_start <= num_max:
    time.sleep(.2)
    device.shell(f"input text {num_start}")
    time.sleep(.2)
    device.shell("input touchscreen tap 998 550")
    print(f"No. Blocked: {num_start}")
    num_start += 1
#



# for contact in contacts:
#
#     message = "Hi [CONTACT_NAME]! This is Therapy Solutions Children's Services reaching out to let you know that our 2022 Summer Camp Registration is now open! Visit our website to learn more! \n\n Click Link: www.TherapySolutionsInc.com/upcoming-events/"
#     message = message.replace("[CONTACT_NAME]",contact[1].split(" ")[0])
#
#
#     device.shell("input tap 975 1865") #Tap NEW MESSAGE button
#     time.sleep(3)
#
#     device.shell("input tap 230 130") #Tap to ENTER PHONE NUMBER
#     device.shell('input text "' + str(contact[0]) + '"')
#     time.sleep(3)
#
#     device.shell("input tap 540 280") #Tap the number that has popped up
#     time.sleep(3)
#
#
#     device.shell("input tap 230 1330") #Tap the MESSAGE box
#     device.shell('input text "' + message + '"')
#     time.sleep(3)
#     device.shell("input tap 1020 1330") #Tap the SEND button
#     time.sleep(3)
#
#     device.shell("input tap 67 93") #Tap the BACK button
#
#     print("MESSAGE SENT TO --------> " + contact[1] + " at " + contact[0])
#     time.sleep(3)