#program  : multi_processing.py
#recipiNo : 7.18
#makeDate : 2019/05/23

import _thread, time, random

def annoy(message):
    while True:
        time.sleep(random.randint(1, 3))
        print(message)
        
_thread.start_new_thread(annoy, ('BOO !!',))

x = 0
while True:
    print(x)
    x += 1
    time.sleep(1)