import os
from threading import Thread
import subprocess

ind = []
net='192.168.40.'
volte = 255


def ping(host):
    print('++++ start ' + net + host)
    #x = subprocess(['ping', net + host])
    x = os.popen('ping ' + net + host).read().split('\n')[2]
    print(x)
    if 'byte' in x:
        ind.append(net + host)
    print('---- stop ' + net + host)
    #non fa il sort
    print(sorted(ind))


for i in range(volte):
    t = Thread(target=ping, args=(str(i+1),))
    t.start()
    
    



