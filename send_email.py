#program  : send_email.py
#recipiNo : 7.16
#makeDate : 2019/05/18

import csv
import smtplib

with open('mail_profile.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        prof = row

GMAIL_USER = prof['GMAIL_USER']
GMAIL_PASS = prof['GMAIL_PASS']
SMTP_SERVER = prof['SMTP_SERVER']
SMTP_PORT = int(prof['SMTP_PORT'])

def send_email(recipient, subject, text):
    smtpserver = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    smtpserver.ehlo()
    smtpserver.starttls()
    smtpserver.ehlo
    smtpserver.login(GMAIL_USER, GMAIL_PASS)
    header = 'To: ' + recipient + '\n' + 'From: ' + GMAIL_USER
    header = header + '\n' + 'Subject: ' + subject + '\n'
    msg = header + '\n' + text + ' \n\n'
    smtpserver.sendmail(GMAIL_USER, recipient, msg)
    smtpserver.close()
    
send_email('receiver@gmail.com', 'sub', 'this is text')