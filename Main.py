#!/usr/bin/python2.7

import os
import ConfigParser
import Mail
import Config
import ExcelDoc


def main():

    # detects if settings.ini is present and creates one if not

    create_config = Config.Config()
    config_path = 'settings.ini'

    if not os.path.exists(config_path):
        create_config.create_config(config_path)

    config = ConfigParser.ConfigParser()
    config.read(config_path)

    # ---------------------Variables under this line-----------------------------------

    user_name = config.get('UserInfo', 'username')
    mail_sender = config.get('UserInfo', 'usermail')
    mail_recipient = config.get('MailRecipient', 'recipient')
    text = 'input something here later'
    attach = 'template-timeliste.ods'
    mail_tester = Mail.Mail()
    workbook = ExcelDoc.ExcelDoc()

    # -------------------Main loop under this line----------------------------------------

    workbook.fill_excel_doc(config_path)

    # Comment out this so i wont flood the mailbox while testing

    # mail_tester.compose_email(mail_recipient, mail_sender, user_name, text, attach)


if __name__ == "__main__":
    main()
