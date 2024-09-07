import time

while True:
    # time watch in 24 hours format
    current_time = time.strftime('%H:%M:%S')
    print(current_time, end='\r')  
    time.sleep(1)  