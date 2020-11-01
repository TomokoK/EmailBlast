#
# Script to automate email blasts for the UWO Tea Club
# 2020-10-14
# contact: TomokoK @ Github
#
import smtplib, ssl
import re

port = 465 # SSL port
senderEmail = input("Enter sender email (e.g. john@gmail.com): ") # Get user details
senderPass = input("Enter sender email password: ")

# Open SSL context
context = ssl.create_default_context()

# Formatting...
#
# Format Subject
subjectFile = open('./boilerplate/emailSubject.txt', 'r')
subject = subjectFile.read()
subjectFile.close()

# Format body
# extract unformatted template
bodyFile = open('./boilerplate/emailBody.txt', 'r')
body = bodyFile.read()
bodyFile.close()
# format the template
bodyFormattingFile = open('./boilerplate/emailBodyFormatting.txt', 'r')
bodyFormatting = bodyFormattingFile.read().split('\n')
bodyFormattingFile.close()
for formatList in bodyFormatting:
    keyword = re.findall(r'\{.*?\}', formatList)
    if keyword in body:
        formattedBody = body.replace(keyword, )

with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
    server.login(senderEmail, senderPass)
    #TODO: Send email here