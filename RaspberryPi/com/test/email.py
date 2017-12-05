import smtplib
import time
from email.message import Message
from time import sleep
import email.utils
import base64

smtpserver = 'smtp.163.com'
username = 'pengjunjie1@163.com'
password = '1123581321'

from_addr = 'pengjunjie1@163.com'
to_addr = '395390646@qq.com'
cc_addr = '1192972761@qq.com'

time = email.utils.formatdate(time.time(),True)

message = Message()
message['Subject'] = 'Mail Subject'
message['From'] = from_addr
message['To'] = to_addr
message['Cc'] = cc_addr
message.set_payload('mail content '+time)
msg = message.as_string()

sm = smtplib.SMTP(smtpserver,port=587,timeout=20)
sm.set_debuglevel(1)
sm.ehlo()
sm.starttls()
sm.ehlo()
sm.login(username, password)

sm.sendmail(from_addr, to_addr, msg)
sleep(5)
sm.quit()