#program  : multi_processing.py
#recipiNo : 7.18
#makeDate : 2019/05/23

import threading, time, random

def annoy(message):
    while True:
        time.sleep(random.randint(1, 3))
        print(message)
        
thread = threading.Thread(target=annoy, args=('BOO !!',))
thread.start()

x = 0
while True:
    print(x)
    x += 1
    time.sleep(1)