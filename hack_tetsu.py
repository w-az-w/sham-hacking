import tqdm
import time
import random

#x=random.randint(1,10)
x=int(random.random()*5+1)

from termcolor import colored

def g_print(*text):
    print(colored(" ".join(text),'white'))


st = time.time()
for wt in [0.005,0.010,0.013]*x:
    #wt = 0.0000001
    for i in tqdm.tqdm(range(50)):
        t = time.time()
        time.sleep(wt)
    print("successful download")
    #g_print(str(t-st),"[sec] is passed")
g_print("hacking completed")
#g_print("c")
#g_print('grn')
#During practice
