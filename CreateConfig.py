import ConfigParser


def createconfig(path):
    """
    create a config file
    :param path:
    :return:
    """
    config = ConfigParser.ConfigParser()
    config.add_section('Settings')
    config.set('Settings', 'Font', 'Courier')
    config.set('Settings', 'font_size', '10')
    config.set('Settings', 'font_info', 'You are using %(font)s at &(font_size)s pt')

    config.add_section('UserInfo')
    config.set('UserInfo', 'Username', raw_input('please enter your name: '))
    config.set('UserInfo', 'Usermail', raw_input('please enter your email: '))

    config.add_section('MailRecipient')
    config.set('MailRecipient', 'Recipient', raw_input('please enter mail recipient: '))
    with open(path, 'wb') as config_file:
        config.write(config_file)

if __name__ == '__main__':
    path = 'settings.ini'
    createconfig(path)
