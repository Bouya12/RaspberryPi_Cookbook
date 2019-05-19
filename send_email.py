#program  : send_email.py
#recipiNo : 7.16
#makeDate : 2019/05/18

import csv
import smtplib

with open('mail_profile.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    prof = row

def send_email(recipient, subject, text):
    smtpserver = smtplib.SMTP(prof['SMTP_SERVER'], int(prof['SMTP_PORT']))
    smtpserver.ehlo()
    smtpserver.starttls()
    smtpserver.ehlo
    smtpserver.login(prof['GMAIL_USER'], prof['GMAIL_PASS'])
    header = 'To: ' + recipient + '\n' + 'From: ' + prof['GMAIL_USER']
    header = header + '\n' + 'Subject: ' + subject + '\n'
    msg = header + '\n' + text + ' \n\n'
    smtpserver.sendmail(prof['GMAIL_USER'], recipient, msg)
    smtpserver.close()
    
send_email('receive@icloud.com', 'sub', 'this is text')