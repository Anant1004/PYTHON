import time
t = time.strftime('%H:%M:%S')
hour = int(time.strftime('%H'))
print(hour)

if(0>=hour<12):
    print("Good Morning, Sir")
elif(12>hour<16):
    print("Good Afternoon, Sir")
elif(17>=hour<19):
    print("Good Evening, Sir")
else:
    print("Good Night, sir")
