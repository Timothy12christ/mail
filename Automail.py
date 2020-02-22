import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText #mime(物件)包下常用的三個模組: text image(圖像) multipart。text常用於製作文字內文
gmail_user='codingbirdno1@gmail.com'
gmail_password='1qazZXCV'
from_address=gmail_user
to_address=['codingbird2018@gmail.com']
Subject="Hi"
contents="ergrgrttg"
mail =MIMEMultipart()
mail['From'] =from_address
mail['To']=','.join(to_address)#指定寄件人的清單
mail['Subject']=Subject
mail.attach(MIMEText(contents))#內文附加在信件中
smtpserver= smtplib.SMTP_SSL("smtp.gmail.com",465)#安全傳輸層通訊附
smtpserver.ehlo()
smtpserver.login(gmail_user,gmail_password)
smtpserver.sendmail(from_address,to_address,mail.as_string())#寄件者的地址，收件者的地址都變成字串
smtpserver.quit()
