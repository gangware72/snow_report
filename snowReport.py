#importing smtplib for email connection
import smtplib, ssl

port = 465 #for SSL
receiver_email = "zachary.feltman@gmail.com"
password = input("Type your password and press enter: ");
message = """\
Subject: Hi there

This message is from Python. """
#creating a secure SSL context
context = ssl.create_default_context();

with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
    server.login("pythonsnowtest@gmail.com", password)
    server.sendmail("pythonsnowtest@gmail.com", receiver_email, message)
    #TODO: Send email here