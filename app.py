import os.path

from src.config_interpreter import read_config, create_config, config_path


# Check if config exists
def main():
    if not os.path.exists(config_path):
        create_config()
    config = read_config()

    print(config['key'])


if __name__ == '__main__':
    main()
