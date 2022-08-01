import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import re
import json

#need to update the html of the email so it's nicer to look at.
def GetEmailFile(email_file):
    with open(email_file, 'r') as open_email:
        email_html = open_email.read()
    return email_html

def MIME_Message(email_sub, send_to, send_from, html_email):
    message = MIMEMultipart('alternative')
    message['To'] = send_to
    message['From'] = ("Jarvis <{}>".format(send_from))
    message['Subject'] = email_sub
    messagebody = MIMEText(html_email, 'html')
    message.attach(messagebody)
    return message.as_string()

def ReplaceContent(Content, message):
    html_output = re.sub("<p>", "<p>" + Content, str(message))
    return html_output

def SendEmail(To, Content):
    File = open("SMTPSettings.json")
    EmailInfo = json.load(File)
    HTMLEmail = GetEmailFile("EmailSample.html")
    HTMLUpdated = ReplaceContent(Content, HTMLEmail)
    Message = MIME_Message("A Message from Jarvis", To, EmailInfo["smtpuser"], HTMLUpdated)
    Server = smtplib.SMTP(EmailInfo["smtpserver"], 587)
    Server.ehlo()
    print("[+] Attempting to say hello")
    Server.login(EmailInfo["smtpuser"], EmailInfo["smtppassword"])
    Server.sendmail("Jarvis <{}>".format(EmailInfo["smtpuser"]), To, Message.encode())
    Server.close()