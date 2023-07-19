import smtplib
#import imghdr
from email.message import EmailMessage

Sender_Email = "codedummy789@gmail.com"
Reciever_list = ["amit.m.kaushik@gmail.com","amit1221kaushik@gmail.com","meenu.kaushik789@gamil.com","meenu.kaushik021@gmail.com"]
Password ="odkznzrmeqqixqbu"

def send_Emails():
    for person in Reciever_list:
        # body=f"""
        #  Hi ! I am Pymail bot . Nice to meet you .
        #  I was created by Shiven kaushik my dev, 
        #  to send emails with a script :)
        #  Hope you love my service :D
        #     """
        
        newMessage = EmailMessage()                         
        newMessage['Subject'] = "Hey I am Pymail :) " 
        newMessage['From'] = Sender_Email                   
        newMessage['To'] = person                 
        newMessage.set_content('Cute cat eh ? . Image attached!') 

        files = ['cute-cat-photo.jpg']

        for file in files:
            with open(file, 'rb') as f:
                image_data = f.read()
                #image_type = imghdr.what(f.name)
                image_name = f.name
            newMessage.add_attachment(image_data, maintype='image', subtype=image_type, filename=image_name)

        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            
            smtp.login(Sender_Email, Password)              
            smtp.send_message(newMessage)                   