import smtplib
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr

def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))

from_addr = 'ywmirai@163.com'
to_addr = '1224759836@qq.com'

msg = MIMEText('邮件正文','plain','utf-8')
# msg['from'] = Header('ywmirai','utf-8')
msg['From'] = 'ywmirai@163.com'
# msg['to'] = Header('接收者显示名字','utf-8')
msg['To'] = _format_addr('管理员 <%s>' % to_addr)
subject = '这是邮件的主题'
msg['Subject'] = Header(subject,'utf-8')

# sender = 'ywmirai@163.com' #发送方邮件地址
# receivers = ['1224759836@qq.com'] #接收放邮件地址，可以为多个
pwd = 'CCOGJQPVNVOWRRJA' # 163smtp授权码

smtpObj = smtplib.SMTP_SSL('smtp.163.com',465)
smtpObj.set_debuglevel(1)
smtpObj.login('ywmirai@163.com',pwd)
# smtpObj.sendmail('ywmirai@163.com',['1224759836@qq.com','qnyhshirann@163.com'],msg.as_string())
smtpObj.sendmail('ywmirai@163.com',msg['to'],msg.as_string())
smtpObj.quit()