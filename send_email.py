
import smtplib, ssl

host = "smtp.gmail.com"
port = 465

username = "tazirxxx@gmail.com"
password = "kcoz erbb ptwi tpmw"

receiver = "tazirxxx@gmail.com"
context = ssl.create_default_context()

message = """\
Subject: Testing Out a 'send_email' Script!
Hi!
How are you?

Sincerely,
Test
"""



with smtplib.SMTP_SSL(host, port, context=context) as server:
    server.login(username, password)
    server.sendmail(username, receiver, message)
