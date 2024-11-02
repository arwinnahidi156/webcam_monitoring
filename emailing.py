import puremagic
import os
from email.message import EmailMessage
import smtplib

def send_email(image_path):
  print("send_email function started")
  
  email_message=EmailMessage()
  email_message['Subject']='New object showed up!'
  email_message.set_content("hey check this object out !")
  
  with open(image_path,'rb') as file:
    content=file.read()
  
  email_message.add_attachment(content,maintype='image',subtype=puremagic.what(None,content))
  
  
  host="smtp.gmail.com"
  port=587
  
  gmail=smtplib.SMTP(host,port)
  gmail.ehlo()
  gmail.starttls()
  username="arwinnahidi156277277@gmail.com"
  password=os.getenv('PASSWORD')
  receiver="arwinnahidi156277277@gmail.com"
  gmail.login(username,password)

  gmail.sendmail(username,receiver,email_message.as_string())
  gmail.quit()
  print("send_email function ended.")
if __name__=='__main__':
  send_email(image_path="images/19.png")

  

