import smtplib
import ssl

#setup port and server name 
smtp_port = 587                  #Standard Secure SMTP Port
smtp_server = 'smtp.gmail.com'   #Google SMTP Server

email_from = "codedummy789@gmail.com"
email_to = "amit.m.kaushik@gmail.com"

pswd = "odkznzrmeqqixqbu"
# Content of message
message = "Hello Papa ye mera email bot :) !"

simple_email_context = ssl.create_default_context()

try:
    print("Connecting to the server ... ")
    TIE_server = smtplib.SMTP(smtp_server,smtp_port)
    TIE_server.starttls(context=simple_email_context)
    TIE_server.login(email_from,pswd)
    print("Connected to server :-) ")

    print()
    print(f"Sending email to - {email_to}")
    TIE_server.sendmail(email_from, email_to, message)
    print(f"Email successfully sent to - {email_to}")

except Exception as e:
    print(e)
finally:
    TIE_server.quit()








