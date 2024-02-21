print("Time Remaining...")
import time

for i in range(30,1,-1):
    # time.sleep(1)
    i=i if i>=10 else "0"+str(i)
    print(i)