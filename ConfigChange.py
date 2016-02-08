import ConfigParser


def updateconfig(path):
    """
    read, update, delete config
    """

    config = ConfigParser.ConfigParser()
    config.read(path)

    # read some values in the config file
    font = config.get('Settings', 'font_size')
    font_size = config.get('Settings', 'font_size')

    # change a value in the config
    config.set('Settings', 'font_size', '12')

    # delete a value from the config
    config.remove_option('Settings', 'font_style')

    # write changes back to the config file
    with open(path, 'wb') as config_file:
        config.write(config_file)

