from email.header import Header
from email.mime.text import MIMEText
msg = MIMEText('hello, send by Python...', 'plain', 'utf-8')
msg['Subject'] = Header("自动化测试报告", 'utf-8')
# 输入Email地址和口令:
# from_addr = input('From: ')
msg['from'] = 'ywmirai@163.com'
# password = input('Password: ')
password = 'CCOGJQPVNVOWRRJA'
# 输入收件人地址:
# to_addr = input('To: ')
msg['to'] = '1224759836@qq.com'
# 输入SMTP服务器地址:
# smtp_server = input('SMTP server: ')
smtp_server = 'smtp.163.com'

import smtplib
server = smtplib.SMTP_SSL(smtp_server,465) # SMTP协议默认端口是25
server.set_debuglevel(1)
server.login(msg['from'], password)
server.sendmail(msg['from'], [msg['to'] ], msg.as_string())
server.quit()