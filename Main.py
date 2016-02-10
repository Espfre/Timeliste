#!/usr/bin/python2.7

import os
import ConfigParser
import Mail
import CreateConfig


def main():

    config_path = 'settings.ini'

    # detects if a config file is present and creates one if not
    if not os.path.exists(config_path):
        CreateConfig.create_config(config_path)

    config = ConfigParser.ConfigParser()
    config.read(config_path)

    # ---------------------Variables under this line-----------------------------------

    user_name = config.get('UserInfo', 'username')
    mail_sender = config.get('UserInfo', 'usermail')
    mail_recipient = config.get('MailRecipient', 'recipient')
    text = 'input something here later'
    attach = 'template-timeliste.ods'
    mail_tester = Mail.Mail()

    # -------------------Main loop under this line----------------------------------------

    # mail_tester.compose_email(mail_recipient, mail_sender, user_name, text, attach)


if __name__ == "__main__":
    main()
