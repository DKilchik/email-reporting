import smtplib
import os

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from utils.html_renderer import HTML


sender = "Private Person <from@example.com>"
receiver = "A Test User <to@example.com>"


# Create message container - the correct MIME type is multipart/alternative.
msg = MIMEMultipart('alternative')
msg['Subject'] = "Link"
msg['From'] = sender
msg['To'] = receiver


root = os.path.dirname(os.path.abspath(__file__))
template = os.path.join(root, 'templates', 'bootstrap.html')
output = os.path.join(root, 'html', 'index.html')

tests = [{"name":"test1", "status":"passed", "duration":"1:01"},
         {"name":"test2", "status":"failed", "duration":"5:01"},
         {"name":"test3", "status":"passed", "duration":"10:01"}]

html = HTML(
    template=template,
    output=output,
    title="Message Title",
    pack_name="Smoke pack",
    total=10,
    passed=5,
    failed=5,
    duration="10:17",
    tests=tests
).render

content = MIMEText(html, 'html')

msg.attach(content)

with smtplib.SMTP("sandbox.smtp.mailtrap.io", 2525) as server:
    server.login("52ed6fcb27d576", "f53926e6784663")
    server.sendmail(sender, receiver, msg.as_string())