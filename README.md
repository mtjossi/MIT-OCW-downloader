# MIT-OCW-downloader
Gets a list of prerequisites of a course, and downloads course material

# Quick Start

Steps:
Download/git clone and unzip. 
Run main.py

Input 1: Course 'Code'*

Input 2: Location where you want to move the folder to.

*Course Code format:*
'/courses/physics/8-06-quantum-physics-iii-spring-2005'  << without quotation marks

'Code' taken from url: ~~https://ocw.mit.edu~~ **/courses/physics/8-06-quantum-physics-iii-spring-2018** ~~/~~

Find courses at: https://ocw.mit.edu/courses/find-by-number/

Happy learning!!




# Additional Details

Required libraries:
>bs4, requests, re, time, os, urllib, shutil, random, wget, pandas, tqdm


## get_links.py

>get_prereq(link_list):

Input: the 'code' to an MIT OCW course where you want to download all prerequisites.
If you provide a 'code' to a course on MIT OCW in the form of /courses/.../...[semester]-[year], the script will get the links to all Prerequisite courses. 

Output: a list of prerequites, and its prerequites, etc.

Note: the path must begin with '/courses/', and end in the year without the final slash (e.g. 'spring-2020'). Without quotation marks!


>clean_list_df(checked_list):

Input: a list of prerequites courses. Will use output of get_prereq() by default.

Output: a pandas dataframe with code-name-season-year and course page link.



## download_courses.py

>download_courses(dataframe_list):

Input: a pandas dataframe with column name 'CourseName' and 'CourseLink'.
clean_list_df() will provide the dataframe. Also can be used to download any OCW course, as long as dataframe with correct format is provided.

Output: Will download course material of all courses in pd.DataFrame. Creates a folder 'Courses', and downloads courses to that folder.

>move_to():

Since the 'Courses' will be default be created in the same directory as the script, you can move the 'Courses' folder to a different directory after downloads are complete.
There will be a prompt to ask where to move the 'Course' folder.
If the default directory is ok, type 'here', or leave blank.


