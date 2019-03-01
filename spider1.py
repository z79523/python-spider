# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 14:51:23 2019

@author: cqde
"""



import threading
import urllib
import os
import requests
from bs4 import BeautifulSoup
import time

gLock = threading.Lock()

# the url of face
FACE_URL_LIST = []

BASE_PAGE_URL = 'https://www.doutula.com/photo/list/?page='
# the url of page
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
    def __init__(self, name, id):
       # self.page_url = page_url
       self.name = name
       self.id = id
    def download_fun(self):
        pass
        #get_page_images(self.page_url)
    
    def get_face_url(self):
        while True:
            gLock.acquire()
            if len(PAGE_URL_LIST) == 0:
                gLock.release()
                break;
            else:
                page_url = PAGE_URL_LIST.pop()
                gLock.release()
                response = requests.get(page_url)
                content = response.content
                soup = BeautifulSoup(content, 'lxml')
                img_list = soup.find_all('img', attrs={'class':'img-responsive lazy image_dta'})
                for img in img_list:
                    #print(type(img))
                    url = img['data-original']
                    if not url.startswith('http'):
                        url = 'http:' + url
                    gLock.acquire()
                    FACE_URL_LIST.append(url)
                    gLock.release()
    def download_face_func(self):
        while True:
            gLock.acquire()
            if len(FACE_URL_LIST) == 0:
                gLock.release()
                continue
            else:
                face_url = FACE_URL_LIST.pop()
                gLock.release()
                split_list = face_url.split('/')
                filename_1 = split_list.pop()
                filename_2 = filename_1.split('!')
                filename = filename_2[0]
               # print(filename)
                path = os.path.join(os.getcwd(), 'images', filename)
                #path = 'C:\Users\cqde\.spyder-py3image\' + filename
                #print(path)
                urllib.request.urlretrieve(face_url, filename=path)
                    
          
        
    
    
       
def main():
    print('start loading img: ', time.ctime())

#    for url in PAGE_URL_LIST:
#        get_page_images(url)
        
    for x in range(3):
        th = threading.Thread(target = threadFunc('producer', x).get_face_url)
        th.start()
#        th.join()
    for x in range(4):
        th = threading.Thread(target = threadFunc('consumer', x).download_face_func)
        th.start()
        #th.join()
  
    print('alive thread num: ', threading.activeCount())
     
    
    print('end loading img: ', time.ctime())
        
       # get_page_images('https://www.doutula.com/photo/list/')
       
       
if __name__ == "__main__":
    main()