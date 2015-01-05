'''
Created on Jan 4, 2015

@author: nb
'''




import imaplib
import getpass

import ConfigParser
from config.getConfigSection import getConfigSection
from _ast import Num
from email import email
from db.DBProcessing import insert_email
from db import DBProcessing

def process_mails(client):
    rv, data = client.search(None,'ALL')
    if rv != 'OK':
        print "No messsage found"
        return 
    for num in reversed(data[0].split()):
        rv, data = client.fetch(num,'(RFC822)')
        if rv != 'OK':
            print "Error in getting message number : ", num
        else :
            msg = email.message_from_string(data[0][1])
            
            #print msg['subject'], "date: ", msg['Date'], msg['From']
            print msg
            DBProcessing.insert_email(data)



gmailConfig = ConfigParser.ConfigParser()
gmailConfig.read("../Gmail_config.ini")
uname = getConfigSection(gmailConfig,"Authentication")['username']
upass = getConfigSection(gmailConfig, "Authentication")['password']

client = imaplib.IMAP4_SSL('imap.gmail.com')
try:
    client.login(uname,upass)
except imaplib.IMAP4.error:
    print("Error occurred while logging in inbox")
print "logged in successfuly to ",uname

rv,mailboxes = client.list()
if rv == 'OK':
    print "mailboxes"
    for mb in mailboxes:
        print mb
rv, data = client.select("INBOX")
if rv == 'OK':
    print "processing mailbox"
    process_mails(client)
else:
    print "Something went wrong"
