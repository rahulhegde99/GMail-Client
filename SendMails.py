# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 16:55:08 2020

@author: Rahul Hegde


"""

#Importing libraries
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

#Initializations
email = "email@gmail.com"

password = "password"
send_to_email = input("Enter recipient's email address\n")

subject = "This is a Computerised Python Mail"

message = input("Enter message\n")

#MIME for email object slicing
msg = MIMEMultipart()
msg['From'] = email
msg['To'] = send_to_email
msg['Subject'] = subject
#Attach the message using a MIMEText object while declaring it as a plain text object
msg.attach(MIMEText(message,'plain'))
 
"""
https://myaccount.google.com/lesssecureapps?pli=1

Go to this link to turn on less secure apps(like Python CLI)
"""

try:
    #Connect to Google's SMTP servers. 587 is the default port number
    server = smtplib.SMTP('smtp.gmail.com',587)
    #Start Transport Layer Security to safely encrypt the password while transporting it from Python client to Google's servers
    server.starttls()
    server.login(email,password)
    
    #Convert the MIMEText message to string and stored in text
    text = msg.as_string()
    
    server.sendmail(email,send_to_email,text)
    server.quit()
    
    print("\nMail sent successfully!")
    
except:
    print("\nBad Request")