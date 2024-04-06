import os.path

from src.config_interpreter import read_config, create_config, config_path
from src.encryption_engine import encrypt, decrypt


def main():
    # Check if config exists
    if not os.path.exists(config_path):
        create_config()

    # Read config
    config = read_config()

    print(decrypt(encrypt('Hello World', config['key']), config['key']))


if __name__ == '__main__':
    main()
