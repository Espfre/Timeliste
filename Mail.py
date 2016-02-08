import base64
import httplib2
import os

from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import Encoders
from email.mime.text import MIMEText
from googleapiclient.discovery import build
from oauth2client.client import flow_from_clientsecrets
from oauth2client.file import Storage
from oauth2client.tools import run_flow
from oauth2client.tools import _CreateArgumentParser


class Mail:

    def __init__(self):
        pass

    def createmessage(self, sender, to, subject, message_text, attach):
        message = MIMEMultipart(message_text)
        message['to'] = to
        message['from'] = sender
        message['subject'] = subject
        message.attach(MIMEText(message_text))
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(open(attach, 'rb').read())
        Encoders.encode_base64(part)
        part.add_header('Content-Disposition',
                        'attachment; filename="%s"' % os.path.basename(attach))
        message.attach(part)

        return {'raw': base64.urlsafe_b64encode(message.as_string())}

    def sendmessage(self, service, user_id, message, attach):
        try:
            message = (service.users().messages().send(userId=user_id, body=message)
                .execute())

            print 'Message Id: %s' % message['id']
            return message
        except Exception as error:
            print 'An error occurred: %s' % error

    def compose_email(self, to, sender, subject, body_text, attach):

        client_secret_file = 'client_secret.json'

        # Check https://developers.google.com/gmail/api/auth/scopes for all available scopes
        oauth_scope = 'https://www.googleapis.com/auth/gmail.compose'

        store = Storage('gmail.storage')

        parser = _CreateArgumentParser()
        flags = parser.parse_args()

        flow = flow_from_clientsecrets(client_secret_file, scope=oauth_scope)
        http = httplib2.Http()

        credentials = store.get()
        if credentials is None or credentials.invalid:
            credentials = run_flow(flow, store, flags, http=http)

        http = credentials.authorize(http)

        gmail_service = build('gmail', 'v1', http=http)
        to_addr = to
        from_addr = sender
        message = self.createmessage(from_addr, to_addr, subject, body_text, attach)
        message = self.sendmessage(gmail_service, 'me', message, attach)
