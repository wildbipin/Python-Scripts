import time

# timestamp = time.strftime('%H:%M:%S')
timestamp = int(time.strftime('%H'))
# print(timestamp)
if timestamp <= 11:
    print("Good Morning")
elif (timestamp >= 12) and ( timestamp <= 17):
    print("Good Afternoon")
elif (timestamp >= 18) and ( timestamp <= 21):
    print("Good Evening")
else:
    print("Good Night")