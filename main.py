# Created by Jordan Leich on 8/10/2020

# Imports
import smtplib
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import colors
import restart

# Globals
to_address = []


# Main code for the program
def main():
    global to_address
    from_address = str(input('What is your email address that you choose to send from: '))
    print()

    if '@' not in from_address.lower() or '.com' not in from_address.lower():
        print(colors.red + 'Error found! Invalid Email Address!\n', colors.reset)
        time.sleep(2)
        restart.restart()

    num_people = int(input('How many people do you wish to email: '))
    print()

    if num_people <= 0:
        print(colors.red+'Error found! Cannot send emails to negative or 0 people!\n', colors.reset)
        time.sleep(2)
        restart.restart()

    for x in range(num_people):
        to_address = str(input('Enter an email address to send to: '))
        print()
        time.sleep(.500)

        if '@' not in to_address.lower() or '.com' not in to_address.lower():
            print(colors.red + 'Error found! Invalid email address!\n', colors.reset)
            time.sleep(2)
            restart.restart()

    msg = MIMEMultipart()
    msg['From'] = from_address
    msg['To'] = " ,".join(to_address)
    msg['subject'] = str(input('Whats the email subject or topic: '))
    print()
    body = str(input('What do you want the body or main text of the email to include: '))
    print()
    msg.attach(MIMEText(body, 'plain', 'utf-8'))
    password = str(input('Enter the password from the sending email to login: '))
    print()
    mail = smtplib.SMTP('smtp.gmail.com', 587)
    mail.ehlo()
    mail.starttls()
    mail.login(from_address, password)
    print(colors.green+'Logged in!\n', colors.reset)
    time.sleep(1)
    text = msg.as_string()
    mail.sendmail(from_address, to_address, text)
    print(colors.yellow + 'Sending mail...\n', colors.reset)
    mail.quit()
    time.sleep(1)
    print(colors.green + 'Email sent successfully!\n', colors.reset)
    time.sleep(1)
    restart.restart()


print(colors.yellow+'Please keep in mind that you can only send emails from a Gmail.com account and you can also send '
                    'these emails to various accounts such as aol, yahoo, outlook, and more!\n', colors.reset)
main()
