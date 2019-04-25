import requests
import re
import os
from pytube import YouTube
from bs4 import BeautifulSoup
import pyfiglet
from colorama import Fore, Back, Style
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}
banner = pyfiglet.figlet_format("WELCOME!!")
print(banner)
print("**********************************")
print("* This is the tool that you can:*\n* -Find the URL in the page     * \n* -Find the IMG URL and Download*\n* -Find the PDF URL and Download*\n* -Download YouTube Video       *")
print("**********************************")
x = raw_input("===>> PASTE the URL (With http:// or https:// ): ")
res = requests.get(str(x), headers=headers)
soup = BeautifulSoup(res.text, "html.parser")
s = x.split('/')
images = []
imgurl = ""
imgurl2 = ""
count = 0
z = []
if res.status_code == 200:
    print('Web site exists')
else:
    print('Web site does not exist')

def getFile(url):
        os.system("wget "+z[i])


def checkexit():
    ans1 =raw_input("Continue or exits:  ")
    if ans1=="continue":
        pass
    else:
        exit
print("\033[;1m What do you want to find?\n1. url in the page\n2. img url in the page\n3. pdf url in the page\n4. Download the youtube video")
y = input()
if y == 1:
    for link in soup.findAll('a', attrs={'href': re.compile('[a-z]+')}):
        a = link.get('href')
        if a == "javascript:void(0)":
            pass
        elif a[0:4] != "http":
            print(s[0]+"//"+s[2]+"/"+link.get('href'))
            count += 1
        else:
            print(link.get('href'))
            count += 1
    checkexit()

elif y == 2:
    for img in soup.findAll('img', attrs={'src': re.compile('[a-z]+')}):
        b = img.get('src')
        z.append(s[0]+"//"+s[2]+"/"+img.get('src'))
        if b[0:4] != "http":
            print(s[0]+"//"+s[2]+"/"+img.get('src'))
            count += 1
        else:
            z.append(img.get('src'))
            print(img.get('src'))
            count += 1
    checkexit()

elif y == 3:
     for link in soup.findAll('a', attrs={'href': re.compile('[a-z]+')}):
        pas = link.get('href')
        if pas == "javascript:void(0)":
            pass
        elif (pas == None or pas.split('.')[-1] != 'pdf'):
		        continue
        elif pas[0:4] != "http":
            z.append(s[0]+"//"+s[2]+"/"+link.get('href'))
            print(s[0]+"//"+s[2]+"/"+link.get('href'))
            count += 1
        else:
            z.append(link.get('href'))
            print(link.get('href'))
            count += 1
     checkexit()
elif y == 4:
    yt = YouTube(x)
    videos = yt.streams.all()
    s = 1
    checkexit()
    for v in videos:
        print(str(s)+". "+str(v))
        s += 1
    n = int(input("Enter the number of the video: "))
    vid = videos[n-1]
    vid.download()
    print("\n successfully downloaded")
    checkexit()

if  y==2 or y==3:
    print("Total link: " + str(count))
    ans = raw_input("Do you want to Download?(Enter: yes or no) ")
    if ans == "yes":
        i = 0
        while i < len(z):
            getFile(z[i])
            i += 1
    else:
        pass

