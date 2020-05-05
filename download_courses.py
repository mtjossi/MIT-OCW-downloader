from bs4 import BeautifulSoup
import requests, re, time, os, urllib, shutil
import pandas as pd
from tqdm import tqdm
import wget


def download_courses(dataframe_list):
    URL = 'https://ocw.mit.edu/'
    for i in tqdm(range(dataframe_list.shape[0])):
        time.sleep(2)
        LINK = dataframe_list.loc[i, 'CourseLink']
        NAME = dataframe_list.loc[i, 'CourseName']
        LOC = './Courses/'
        r = requests.get(URL + LINK + '/download-course-materials/')
        soup = BeautifulSoup(r.content, 'lxml')

        button = soup.find(class_='downloadNowButton')
        dl = button.get('href')

        wget.download(f"{URL+dl}", f"{LOC}/{NAME}.zip")
        # os.system(f'wget -O {LOC}/{NAME} {URL+dl}')
    print('\n')
    print('Downloaded all courses!')


def move_to():
    DEST = input('Please state where you want to move the files to... \n')
    if (DEST == '') or (DEST == 'here'):
        pass
    else:
        shutil.move('./Courses', DEST)

    print('Done.')
