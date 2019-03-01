# -*- coding: utf-8 -*-
"""
Created on Thu Feb 28 16:34:53 2019

@author: cqde
"""


import threading
import urllib
import os
import requests
from bs4 import BeautifulSoup
import time

BASE_PAGE_URL = 'https://www.doutula.com/photo/list/?page='
PAGE_URL_LIST = []
for x in range(1, 5):
    url = BASE_PAGE_URL + str(x)
    PAGE_URL_LIST.append(url)
    
    

    
def download_image(url):
    split_list = url.split('/')
    filename_1 = split_list.pop()
    filename_2 = filename_1.split('!')
    filename = filename_2[0]
   # print(filename)
    path = os.path.join(os.getcwd(), 'images', filename)
    #path = 'C:\Users\cqde\.spyder-py3image\' + filename
    #print(path)
    urllib.request.urlretrieve(url, filename=path)
    
#download_image('http://img.doutula.com/production/uploads/image//2019/02/28/20190228320309_AZaMKd.gif!dta')

def get_page_images(page_url):
    response = requests.get(page_url)
    content = response.content
    soup = BeautifulSoup(content, 'lxml')
    img_list = soup.find_all('img', attrs={'class':'img-responsive lazy image_dta'})
    for img in img_list:
        #print(type(img))
        url = img['data-original']
        #print(url)
        download_image(url)
       # 
class threadFunc:
    def __init__(self, page_url):
        self.page_url = page_url
    def download_fun(self):
        get_page_images(self.page_url)
    
    
       
def main():
    thread_list = []
    print('start loading img: ', time.ctime())

#    for url in PAGE_URL_LIST:
#        get_page_images(url)
        
    for url in PAGE_URL_LIST:
        thr = threading.Thread(target = threadFunc(url).download_fun)
        thread_list.append(thr)
        thr.start()
    
    print('alive thread num: ', threading.activeCount())
    for thr in thread_list:
        thr.join()
        print(thr.getName())
    print('alive thread num: ', threading.activeCount())
     
    
    print('end loading img: ', time.ctime())
        
       # get_page_images('https://www.doutula.com/photo/list/')
       
       
if __name__ == "__main__":
    main()


    