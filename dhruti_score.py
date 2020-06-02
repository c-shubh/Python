# Gets score from the spreadsheet on https://docs.google.com/spreadsheets/d/1Rw2q0dlCSGjaggUArkgXRPEHacGrH0855HfSyVBd6Ek/edit#gid=1541449767 and displays the score as a table.

import requests
from bs4 import BeautifulSoup
from tabulate import tabulate
import os
from msvcrt import getch
os.system('mode 1000')
URL = 'https://docs.google.com/spreadsheets/d/1Rw2q0dlCSGjaggUArkgXRPEHacGrH0855HfSyVBd6Ek/edit#gid=1541449767'

headers = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.113 Safari/537.36'}
page = requests.get(URL, headers=headers)

soup = BeautifulSoup(page.content, 'html.parser')

title = soup.find(id='waffle-grid-container').get_text(" ")
title = list(title.split())
index = title.index('18881A1274')
dhruti_details = title[index:][:27]
del title
for i in [23, 21, 20, 18, 17, 16, 14, 13, 12, 10, 9, 8, 6, 4, 3, 2]:
    del dhruti_details[i]
del dhruti_details[1:4]
dhruti_details.insert(1, 'Dhruti A Chudasama')
empty = []
empty.append(dhruti_details)
headers = ['Roll Number', 'Student Name', 'HackerRank', 'Codechef',
           'Codeforces', 'Spoj', 'InterviewBit', 'Basic HackerRank', 'Overall Score']
print('\n\n' + tabulate(empty, headers=headers))
print("\n\nPress any key to exit...")
exit = getch()
