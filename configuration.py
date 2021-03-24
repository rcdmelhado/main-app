import os
import configparser

configfile_name = "config.ini"

if not os.path.isfile(configfile_name):
    with open(configfile_name, "w") as config_file:
        config = configparser.ConfigParser()
        config['rabbitmq'] = {'uri': ''}
        config.write(config_file)
