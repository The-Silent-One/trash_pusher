import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv
load_dotenv()
import os

port = 465
sender = os.getenv("SENDER")
password = os.getenv("PASSWORD")
receiver = os.getenv("RECEIVER")
context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
    msg = MIMEMultipart("alternative")
    msg["subject"] = "[Test] Automatic reminder"
    msg["From"] = sender
    msg["To"] = receiver
    html = """
    <html><body><h2>
    This is a friendly reminder to log in linux so that it can automaticaly push to 
    <a href="https://github.com/The-Silent-One/trash_pusher">git</a>
    <br><br>
    Pushing for letter
    </h2></body></html>"""
    
    part = MIMEText(html, "html")
    
    msg.attach(part)
    
    server.login(sender, password)
    server.sendmail(sender,receiver,msg.as_string())
    
