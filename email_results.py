import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class sending_email():
    def send_email(self, contents):
        mail_content = "Your Inventory list is here"

        sender_address = "SIKRacer@gmail.com"
        sender_pass = "Bugatti89"
        receiver_address = "SIKRacer@gmail.com"

        message = MIMEMultipart()
        message['From'] = sender_address
        message['To'] = receiver_address
        message['Subject'] = "Inventory List"

        message.attach(MIMEText(contents, 'plain'))

        session = smtplib.SMTP('smtp.gmail.com', 587)
        session.starttls()
        session.login(sender_address, sender_pass)
        text = message.as_string()
        session.sendmail(sender_address, receiver_address, text)
        session.quit()