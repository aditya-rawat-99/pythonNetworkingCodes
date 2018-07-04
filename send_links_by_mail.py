import getpass, shelve
import os, pyperclip, smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication


def send_mail(sender, recipient):


    session = smtplib.SMTP("smtp.gmail.com", 587)
    session.ehlo()
    session.starttls()
    password = str(getpass.getpass(prompt="Enter password: "))
    session.login(sender, password)

    msg = MIMEMultipart()
    msg["To"] = recipient
    msg["From"] = sender
    subject = str(input("Enter subject: "))
    msg["Subject"] = subject
    message = ""
    for values in shelf.values():
        message = message +  values + "\n"

    part = MIMEText("text", "plain")
    part.set_payload(message)
    msg.attach(part)
    session.sendmail(sender, recipient, msg.as_string())

    session.close()


if __name__ == "__main__":
    os.chdir("/home/aditya/Downloads")
    shelf = shelve.open("links")

    shelf.clear()

    print("Press CTRL-C to exit")
    while True:
        try:
            if pyperclip.paste() not in shelf.values():
                shelf[str(pyperclip.paste()[-25:-6])] = pyperclip.paste()
            else:
                continue
        except KeyboardInterrupt as KeyE:
            print("Exited: " + str(KeyE))
            break

    sender = str(input("Enter sender's email: "))
    recipient = str(input("Enter recipient's email: "))
    send_mail(sender, recipient)
    shelf.close()
