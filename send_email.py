#program  : send_email.py
#recipiNo : 7.16
#makeDate : 2019/05/18

import csv
import smtplib
from email.mime.text import MIMEText
from email.header import Header

charset = 'iso-2022-jp'

with open('mail_profile.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        prof = row

def send_email(recipient, subject, text):

    msg = MIMEText(message, 'plain', charset)
    msg['Subject'] = Header(subject.encode(charset), charset)

    smtpserver = smtplib.SMTP(prof['SMTP_SERVER'], int(prof['SMTP_PORT']))
    smtpserver.ehlo()
    smtpserver.starttls()
    smtpserver.login(prof['GMAIL_USER'], prof['GMAIL_PASS'])
    smtpserver.sendmail(prof['GMAIL_USER'], recipient, msg.as_string())
    smtpserver.close()


reciever = input('送信先メールアドレスを入力してください：')
subject = input('件名を入力してください：')
message = input('メッセージを入力してください：')
send_email(reciever, subject, message)
