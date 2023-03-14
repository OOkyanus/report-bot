import smtplib, ssl, pickle
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def pickle_dump(data, path):
    with open(path, 'wb') as fp:
        pickle.dump(data, fp)

def pickle_load(path):
    with open(path, 'rb') as fp:
        return pickle.load(fp)

def setReporterInfo(path):
    if not path.endswith('/'):
        path=path+'/'

    
    sender_email = input('Enter your report-bot email: ')
    password = input('Enter your email\'s app-password: ')
    receiver_email = input('Enter the default receiver email: ')
    subject = input('Enter the default subject: ')

    reporter_info={'sender_email':sender_email,
                    'password': password,
                    'receiver_email': receiver_email,
                    'subject':subject}

    pickle_dump(reporter_info,path+'RPRTR.INFO')

class Reporter():
    def __init__(self, reporter_info_path):

        if not reporter_info_path.endswith('/'):
            reporter_info_path=reporter_info_path+'/'

        self.port = 465  # For SSL
        self.login_info=pickle_load(reporter_info_path+'RPRTR.INFO')

        # Create a secure SSL context
        self.context = ssl.create_default_context()

    def sendmail(self,text_message,subject=None,receiver_email=None):
        with smtplib.SMTP_SSL("smtp.gmail.com", self.port, context=self.context) as server:
            server.login(self.login_info['sender_email'], self.login_info['password'])

            msg = MIMEMultipart()
            msg['From'] = self.login_info['sender_email']            
            msg['To'] = receiver_email if receiver_email is not None else self.login_info['receiver_email']
            msg['Subject'] = subject if subject is not None else self.login_info['subject']

            body = text_message
            msg.attach(MIMEText(body, 'plain'))

            text = msg.as_string()

            server.sendmail(self.login_info['sender_email'], msg['To'], text)

if __name__ == "__main__":

    setReporterInfo('.../path2reporterInfoFolder') # RUN ONCE

    bot=Reporter('.../path2reporterInfoFolder')
    bot.sendmail(text_message='a message', subject='My Extremely Original Subject', receiver_email='receiver@anymail.com')
