# Simple SMTP Client using Python 
# SMTP lib plus SSL

import smtplib
import ssl 
from time import sleep

from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Main body here
subject = input('Subject:')
body = input('')
sender_email = input('Your Email:')
receiver_email = input('To:')
password = input('password:')
# create the message 
message = MIMEMultipart()
message["From:"] = sender_email
message["To:"] = receiver_email
message["Subject:"] = subject
message["BCC:"] = receiver_email
message.attach(MIMEText(body,"plain")) # Attach the text message here
filename = "sample.txt" # edit this on the file path of your attachment
with open(filename,'rb') as attachment:
    part = MIMEBase("application","octet-stream")
    part.set_payload(attachment.read())
encoders.encode_base64(part)
part.add_header(
    "Content-Disposition",
    "attachment; filename = {filename}",
)
# attach the attachment here
message.attach(part)
text = message.as_string()
# initialize connection to the email server
context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com",465,context=context) as server:
    server.login(sender_email,password)
    server.sendmail(sender_email,receiver_email,text)
