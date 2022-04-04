import smtplib, email, imaplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from config import login_, password_

class EmailClient:
    def __init__(self, login_, password_):
        self.connect = {'login': login_, 'password': password_}

    def send_mail(self, message_, subject_, recipient_):
        try:
            email = MIMEMultipart()
            email['From'] = self.connect['login']
            email['To'] = recipient_
            email["Subject"] = subject_
            email.attach(MIMEText(message_))
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.ehlo()
            server.starttls()
            server.ehlo()
            server.login(self.connect['login'], self.connect['password'])
            server.sendmail(email['From'], email['To'], email.as_string())
        except Exception as _ex:
            return f'{_ex}\nПроверь логин или пароль'

    def receiving_mail(self, mailbox_):
        receiving_mail = imaplib.IMAP4_SSL("imap.gmail.com")
        try:
            receiving_mail.login(self.connect['login'], self.connect['password'])
            receiving_mail.select(mailbox_)
            result, data = receiving_mail.search(None, "ALL")
            ids = data[0]
            id_list = ids.split()
            last_email_id = id_list[-1]
            result, data = receiving_mail.fetch(last_email_id, '(RFC822)')
            raw_email = data[0][1]
            raw_email_string = raw_email.decode('utf-8')
            email_message = email.message_from_string(raw_email_string)
            print(email_message['To'])
            # print(email.utils.parseaddr(email_message['From']))
            # print(email_message['Date'])
            print(email_message['Subject'])
            # print(email_message['Message-Id'])
            if email_message.is_multipart():
                for payload in email_message.get_payload():
                    body = payload.get_payload(decode=True).decode('utf-8')
                    print(body)
            else:
                body = email_message.get_payload(decode=True).decode('utf-8')
                print(body)
        except Exception as _ex:
            return f'{_ex}\nПроверь логин или пароль'



if __name__ == "__main__":
    gmail = EmailClient(login_, password_)
    subject = input("Введите тему сообщения: ")
    message = input("Введите сообщение: ")
    recipient_ = input("Адрес получателя:")
    print(gmail.send_mail(message, subject, recipient_))
    print(gmail.receiving_mail('INBOX'))


