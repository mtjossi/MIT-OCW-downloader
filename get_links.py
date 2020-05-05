from bs4 import BeautifulSoup
import requests, time, random
import pandas as pd


def waitt():
    time.sleep(round(random.random() * 5, 2))


def get_prereq(link_list):
    global count
    global len_list
    url = 'https://ocw.mit.edu'
    if len(link_list) == 0:
        print('Finished getting all links!')

    else:
        waitt()
        r = requests.get(url + link_list[0] + '/syllabus/')
        soup = BeautifulSoup(r.text, 'lxml')
        p1 = soup.find(id='course_inner_section')
        try:
            p2 = p1.find_all_next('a')
            ll = []
            for p in p2:
                pp = p.get('href')

                ll.append(pp)

        except:
            ll = []

        if link_list[0] not in checked_list:
            checked_list.append(link_list[0])
            link_list.remove(link_list[0])
        else:
            link_list.remove(link_list[0])

        for l in ll:

            if ('/courses/' in l):
                if (l[-1] in '0123456789'):
                    link_list.append(l)
                elif (l[-9:] == 'index.htm'):
                    link_list.append(l[:-10])
        count += 1
        print(f'round {count}...')
        len_list.append(len(checked_list))
        if count > 5:
            if len_list[-1] == len_list[-3]:
                link_list = []

        get_prereq(link_list)

    return link_list, checked_list


def clean_list_df(checked_list):
    if len(checked_list) == len(list(checked_list)):

        name_list = []

        for i in checked_list:
            name_list.append((i.split('/')[-1]))

        df = pd.DataFrame({'CourseName': name_list,
                           'CourseLink': checked_list})
        print('Finished cleaning!')
        return df
    else:
        print('There might be a problem...')



count = 0
len_list = []

link_list = []
checked_list = []
