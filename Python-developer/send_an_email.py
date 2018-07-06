import smtplib
from email.mime.text import MIMEText
_user = "1534002786@qq.com"
_pwd = "cnlgguamojobifgf"

_to = str(input('select the email address you want to send\n'))
subject = str(input('this is your subject\n'))
content = str(input('this is your content\n'))

msg = MIMEText(content)
msg["Subject"] = subject
msg["From"] = _user
msg["To"] = _to

try:
    s = smtplib.SMTP_SSL("smtp.qq.com", 465)
    s.login(_user, _pwd)
    s.sendmail(_user, _to, msg.as_string())
    s.quit()
    print("Success!")
except smtplib.SMTPException as e:
    print ('error', e)