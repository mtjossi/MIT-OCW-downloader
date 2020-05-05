from bs4 import BeautifulSoup
import requests, re, time, os, urllib, shutil, random, wget
import pandas as pd
from tqdm import tqdm


from get_links import get_prereq, clean_list_df
from download_courses import download_courses, move_to



# global checked_list

count = 0
len_list = []

link_list = []
checked_list = []

start_link = input('Which course do you want to start with? \n')

link_list.append(str(start_link))

ll, cl = get_prereq(link_list)

df = clean_list_df(cl)

df.to_csv('./prereq_list.csv', index=False)


df = pd.read_csv('./prereq_list.csv')
if 'Courses' not in os.listdir():
    os.mkdir('./Courses')
download_courses(df)
move_to()
