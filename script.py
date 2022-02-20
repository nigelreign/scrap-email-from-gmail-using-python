import imaplib
import email
from email.header import decode_header
import webbrowser
import os

# account credentials
username = "test@gmail.com"
password = "mypassword"

# create an IMAP4 class with SSL 
imap = imaplib.IMAP4_SSL("imap.gmail.com")

# authentication
imap.login(username, password)

# email address to get emails from
emails_from = "target@gmail.com"

status, messages = imap.select("INBOX")

# number of top emails to fetch
number = 10
# total number of emails
messages = int(messages[0])

for i in range(messages, messages-number, -1):
    # fetch the email message by ID
    res, msg = imap.fetch(str(i), "(RFC822)")
    for response in msg:
        if isinstance(response, tuple):
            # parse a bytes email into a message object
            msg = email.message_from_bytes(response[1])
            # decode the email subject
            subject, encoding = decode_header(msg["Subject"])[0]
            if isinstance(subject, bytes):
                # if it's a bytes, decode to str
                subject = subject.decode(encoding)
            # decode email sender
            From, encoding = decode_header(msg.get("From"))[0]
            if isinstance(From, bytes):
                From = From.decode(encoding)

            start = From.find("<") + len("<")
            end = From.find(">")
            search_email = From[start:end]
            print(search_email)
            if search_email == emails_from:
                # if the email message is multipart
                if msg.is_multipart():
                    pass    
                else:
                    # extract content type of email
                    content_type = msg.get_content_type()
                    # get the email body
                    body = msg.get_payload(decode=True).decode()
                    if content_type == "text/plain":
                        # print only text email parts
                        print(body)

                print("="*100)
            else:
                pass
# close the connection and logout
imap.close()
imap.logout()
