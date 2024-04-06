import configparser
from typing import Final

config_path:Final[str] = 'config.cfg'

# Config file:
# [DEFAULT]
# key = value
# file-location = /path/to/file
# encrypted-file-location = /path/to/encrypted_file
# decrypted-file-location = /path/to/decrypted_file
# use_compression = True/False
def create_config():
    config = configparser.ConfigParser()
    config['DEFAULT'] = {'key': '123456789aa',
                         'file-location': './message.txt',
                         'encrypted-file-location': './encrypted_message.txt',
                         'decrypted-file-location': './decrypted_message.txt',
                         'use_compression': 'False'}

    with open(config_path, 'w') as configfile:
        config.write(configfile)

def read_config():
    config = configparser.ConfigParser()
    config.read(config_path)
    return config['DEFAULT']