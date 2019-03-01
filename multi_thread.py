# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 09:17:43 2019

@author: cqde
"""
import threading as thread
import time

def greet(thread_name, index):
    print(thread_name + ': ' + str(index))
    time.sleep(1)
    
    
def line_run():
    for i in range(5):
        greet('line_run', i)
        
        
        
        
def async_run():
    threadNum = []
    for i in range(5):
        t = thread.Thread(target=greet, args={'async', str(i), })
        t.start()
        threadNum.append(t)
    for t in threadNum:
        t.join()
        


        
if __name__ == "__main__":
    #line_run()
    async_run()
    print('end run')