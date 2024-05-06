import smtplib, ssl # smtplib-simple mail transfer protocol
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import  MIMEText
from typing import Final

import os
from dotenv import load_dotenv

load_dotenv()

EMAIL: Final[str] = os.environ.get("EMAIL")
PASSWORD: Final[str] = os.environ.get("PASSWORD")


def create_image_attachment(path: str) -> MIMEImage:
    with open(path, 'rb') as image:
        mime_image = MIMEImage(image.read())
        mime_image.add_header('Content-Disposition', f'attachment; filename={path}')
        return mime_image


def send_email(
        to_email: str,
        subject: str,
        body: str,
        image: str | None = None
):
    host: str = 'smtp-mail.outlook.com'
    port: int = 587

    context = ssl.create_default_context()

    with smtplib.SMTP(host, port) as server:
        print('Logging in...')
        server.ehlo()
        server.starttls(context=context)
        server.ehlo()
        server.login(EMAIL, PASSWORD)

        # Prepare email
        print('Attempting to send email')
        message = MIMEMultipart()
        message['From'] = EMAIL
        message['To'] = to_email
        message['Subject'] = subject
        message.attach(MIMEText(body, 'plain'))

        if image:
            file: MIMEImage = create_image_attachment(image)
            message.attach(file)

        server.sendmail(from_addr=EMAIL, to_addrs=to_email, msg=message.as_string())

        print('Sent!')


if __name__ == '__main__':
    send_email(
        to_email='luismario190224@gmail.com',
        subject='Hello there!',
        body='How have you been? Take a look at this cute cat',
        image='cat.png'
    )