import smtplib
from email.message import EmailMessage
from speak import *

my_email = "my_email_add"
password = "my_email_pw"


def send_email(recipient, subject, message):
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        email = EmailMessage()
        email['From'] = my_email
        email['To'] = recipient
        email['Subject'] = subject
        email.set_content(message)

        connection.send_message(email)


email_list = {
    'amy': '******.edu',
    'rina': '*******.com'
}


def mail_info():
    speak("Who would you like to send the email to?")
    name = take_command()
    recipient = email_list[name]
    print(recipient)
    speak("What is the subject of the email?")
    subject = take_command()
    speak("What should go in the body of the email?")
    message = take_command()
    send_email(recipient, subject, message)
    speak("Your email has been sent")