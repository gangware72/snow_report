#importing smtplib for email connection
import smtplib, ssl
import os
import requests #not sure this was included in my pip package


WEATHER_API_KEY = "edc847f9ce1a6cd925d05222f0fd06bd"
LATITUDE = "39.742043"
LONGITUDE = "-104.991531"
port = 465 #for SSL
receiver_email = "zachary.feltman@gmail.com"
password = input("Type your password and press enter: ");
message = """\
Subject: Hi there

This message is from Python. """
#creating a secure SSL context
context = ssl.create_default_context();

#TODO: lower securty of GMAIL account. Can't find where to do that.
with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
    server.login("pythonsnowtest@gmail.com", password)
    server.sendmail("pythonsnowtest@gmail.com", receiver_email, message)
    #TODO: Send email here
    
    
if __name__ == "__main__":
    resp = requests.get(f"https://api.openweathermap.org/data/3.0/onecall?lat={LATITUDE}&lon=-{LONGITUDE}&appid={WEATHER_API_KEY}")
    
    forecast = resp.json()['hourly'][0]