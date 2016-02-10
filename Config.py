import ConfigParser
import datetime


class Config:

    def __init__(self):
        pass

    def create_config(self, path):
        """
        create a config file
        :param path:
        :return:
        """
        dt = datetime.datetime.today()
        config = ConfigParser.ConfigParser()

        config.add_section('General')
        config.set('General', 'Weeknumber', dt.strftime('%U'))

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

    def update_week(self, path):
        """
        read, update, delete config
        :param path:
        :return:
        """

        config = ConfigParser.ConfigParser()
        config.read(path)

        dt = datetime.datetime.today()
        config.set('General', 'Weeknumber', dt.strftime('%U'))

        with open(path, 'wb') as config_file:
            config.write(config_file)

    def update_config(self, path):
        """
        read, update, delete config
        :param path:
        :return:
        """

        config = ConfigParser.ConfigParser()
        config.read(path)

        # read some values in the config file
        # font = config.get('Settings', 'font_size')
        # font_size = config.get('Settings', 'font_size')

        # change a value in the config
        # config.set('Settings', 'font_size', '12')

        # delete a value from the config
        # config.remove_option('Settings', 'font_style')

        # write changes back to the config file
        with open(path, 'wb') as config_file:
            config.write(config_file)
