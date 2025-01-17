#Following Links in Python
#In this assignment you will write a Python program that expands on
#http://www.pythonlearn.com/code/urllinks.py. The program will use urllib to
#read the HTML from the data files below, extract the href= vaues from the anchor
#tags, scan for a tag that is in a particular position relative to the first name
#in the list, follow that link and repeat the process a number of times and report
#the last name you find.
#We provide two files for this assignment. One is a sample file where we give you
#the name for your testing and the other is the actual data you need to process
#for the assignment
#Sample problem: Start at http://python-data.dr-chuck.net/known_by_Fikret.html
#Find the link at position 3 (the first name is 1). Follow that link. Repeat this
#process 4 times. The answer is the last name that you retrieve.
#Sequence of names: Fikret Montgomery Mhairade Butchi Anayah
#Last name in sequence: Anayah
#Actual problem: Start at: http://python-data.dr-chuck.net/known_by_Blanka.html
#Find the link at position 18 (the first name is 1). Follow that link. Repeat
#this process 7 times. The answer is the last name that you retrieve.
#Hint: The first character of the name of the last page that you will load is: L


import urllib.request as ur
from bs4 import *

current_repeat_count = 0
url = input('Enter URL: ')
repeat_count = int(input('Enter count: '))
position = int(input('Enter position: '))


def parse_html(url):
    html = ur.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    return tags

while current_repeat_count < repeat_count:
    print('Retrieving: ', url)
    tags = parse_html(url)
    for index, item in enumerate(tags):
        if index == position - 1:
            url = item.get('href', None)
            name = item.contents[0]
            break
        else:
            continue
    current_repeat_count += 1
print('Last Url: ', url)
