import smtplib
import os
import argparse

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from utils.html_renderer import HTML

parser = argparse.ArgumentParser(description="cmd parameters",
                                 formatter_class=argparse.ArgumentDefaultsHelpFormatter)

parser.add_argument("-s", "--sender", action="store", default="<from@example.com>", help="email sender")
parser.add_argument("-r","--receiver", action="store", default="<to@example.com>", help="email receivers, comma separated list")
parser.add_argument("--subject", action="store", default="Test execution report", help="email subject")
parser.add_argument("-t","--title", action="store", default="E-Shop", help="email title")
parser.add_argument("-p","--pack", action="store", default="Smoke pack", help="testing pack")
parser.add_argument("-f","--reports_folder", action="store", default="/target/cucumber-reports", help="path to folder with reports")

args = parser.parse_args()

config = vars(args)
print(config)


# with smtplib.SMTP("sandbox.smtp.mailtrap.io", 2525) as server:
#     server.login("52ed6fcb27d576", "f53926e6784663")
#     server.sendmail(sender, receiver, msg.as_string())