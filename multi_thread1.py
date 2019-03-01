# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 10:05:51 2019

@author: cqde
"""

import threading
from time import sleep, ctime


loop = [4, 2]

class ThreadFunc:
    def __init__(self, name):
        self.name = name
        
    def loop(self, nloop, nsec):
        '''
        nloop: the name of function
        nsec: sleep time
        '''
        print('Start loop', nloop, 'at ', ctime())
        sleep(nsec)
        print('Done loop', nloop, 'at ', ctime())
    
def main():
    print('Start at: ', ctime())
    
    # ThreadFunc("loop")
    # t = ThreadFunc("loop")
    # t.loop
    
    t = ThreadFunc("loop")
    t1 = threading.Thread(target = t.loop, args = ('loop1', 4))
    t2 = threading.Thread(target = ThreadFunc('loop').loop, args = ('loop2', 2))
     
    # error 
    '''
    t1 = treading.Thread(target=ThreadFunc('loop').loop(100, 4))
    t2 = treading.Thread(target=ThreadFunc('loop').loop(100, 4))
    '''
    
    t1.start()
    t2.start()
    
    t1.join()
    t2.join()
    
    print('All done at: ', ctime())
    
if __name__ == "__main__":
    main()
    