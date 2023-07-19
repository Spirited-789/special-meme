import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders



#setup port and server name 
smtp_port = 587                  #Standard Secure SMTP Port
smtp_server = 'smtp.gmail.com'   #Google SMTP Server

email_from = "codedummy789@gmail.com"
email_list = ["amit.m.kaushik@gmail.com","amit1221kaushik@gmail.com","meenu.kaushik789@gamil.com","meenu.kaushik021@gmail.com"]


pswd = "odkznzrmeqqixqbu"

Subject = "Pymail bot testing 1"

def send_emails(email_list):
    for person in email_list:
        #Making body of email

        body = f""" 
         Hi ! I am Pymail bot . Nice to meet you .
         I was created by Shiven kaushik my dev, 
         to send emails with a script :)
         Hope you love my service :D
         """

        #Make a mime object to define parts of the email
        msg = MIMEMultipart()
        msg['From'] = email_from
        msg['To'] = person
        msg['Subject'] = Subject
    
        #Attach the body of the message
        msg.attach(MIMEText(body,'plain'))

        # Define the file to attach
        filename = "cute-cat-photo.jpg"


        #open the file in python in binary format
        attachment= open(filename,'rb') #r for read and b for binary

        # Encode as base 64
        attachment_package = MIMEBase('application','octet-stream')
        attachment_package.set_payload((attachment).read())
        encoders.encode_base64(attachment_package)
        attachment_package.add_header('Content-Disposition',"attachment; filename- "+ filename)
        msg.attach(attachment_package)
        
        #cast as string
        text = msg.as_string()
         
        #connecting with the server
        print("Connecting to the server ...")
        TIE_server = smtplib.SMTP(smtp_server,smtp_port)
        TIE_server.starttls()
        TIE_server.login(email_from,pswd)
        print("Successfully connected to the server :) ")
        print()
        
        #sending emails to "person" as list is iterated
        print(f"Sending email to: {person}...")
        TIE_server.sendmail(email_from,person,text)
        print(f"Email sent to: {person}")
        print()

    TIE_server.quit()

send_emails(email_list)



         



