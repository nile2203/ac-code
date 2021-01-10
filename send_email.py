import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class SendEmail:
	SENDER_EMAIL = 'testing.email90011@gmail.com'
	SENDER_PASSWORD = 'tester@1234'
	DEFAULT_HOST = 'smtp.gmail.com'
	DEFAULT_PORT = 587

	def __init__(self, receiver_email, subject, message):
		self.subject = subject
		self.receiver_email = receiver_email
		self.message = message
		self.smtp = SendEmail.setup_smtp()

	@staticmethod
	def setup_smtp():
		smtp = smtplib.SMTP(host=SendEmail.DEFAULT_HOST, port=SendEmail.DEFAULT_PORT)
		smtp.starttls()
		smtp.login(SendEmail.SENDER_EMAIL, SendEmail.SENDER_PASSWORD)
		return smtp

	def send(self):
		raw_message = MIMEMultipart()
		raw_message['From'] = SendEmail.SENDER_EMAIL
		raw_message['To'] = self.receiver_email
		raw_message['Subject'] = self.subject

		plain_text = MIMEText(self.message, 'plain', _charset='UTF-8')
		raw_message.attach(plain_text)

		self.smtp.send_message(raw_message)
		self.smtp.quit()
		return 1, 'Email Sent!'

def main():
	subject = input("Subject? ")
	message = input("Body? ")
	receiver_email = input("Recipient? ")
	status, message = SendEmail(receiver_email=receiver_email, subject=subject, message=message).send()
	print(message)

if __name__ == '__main__':
	main()


