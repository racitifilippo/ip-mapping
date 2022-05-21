import os
from threading import Thread
import subprocess

ind = []
net = ''
while 1:
    try:
        net= input('Scrivere indirizzo ipv4 senza lultimo ottetto valido: ')
    except:
        1
    n = 0
    for i in range(len(net)):
        if net[i] == '.':
            n += 1
    if n == 3 :
        break

volte = 255


def ping(host):
    print('++++ start ' + net + host)
    #x = subprocess(['ping', net + host])
    x = os.popen('ping -c 3 ' + net + host).read().split('\n')[2]
    print(x)
    if 'byte' in x:
        ind.append(net + host)
    print('---- stop ' + net + host)
    #non fa il sort
    print(sorted(ind))


for i in range(volte):
    t = Thread(target=ping, args=(str(i+1),))
    t.start()
    
    



