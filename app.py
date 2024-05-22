import os.path
from src.config_interpreter import read_config, create_config, config_path
from src.encryption_engine import encrypt, decrypt


def main():
    # Check if config exists
    if not os.path.exists(config_path):
        create_config()

    # Read config
    config = read_config()

    # User menu
    # 1. Encrypt message
    # 1.1 Use config
    # 1.2 User values
    # 2. Decrypt message
    # 2.1 Use config
    # 2.2 User values
    # 3. Exit

    while True:
        print('1. Encrypt message')
        print('2. Decrypt message')
        print('3. Exit')
        choice = input('#> ')

        match choice:
            case '1':
                print('1. Use config location and key')
                print('2. User values')
                choice = input('#> ')

                text = ""
                key = ""
                save_location = ""

                match choice:
                    case '1':
                        text = open(config['file-location'], 'r').read()
                        save_location = config['encrypted-file-location']
                        key = config['key']
                    case '2':
                        text = open(input('Enter file location: '), 'r').read()
                        save_location = input('Enter save location: ')
                        key = input('Enter key: ')

                # Encrypt text
                encrypted_text = encrypt(text, key)
                # Save encrypted text
                f = open(save_location, 'w')
                f.write(encrypted_text)
                f.close()
            case '2':
                print('1. Use config location and key')
                print('2. User values')
                choice = input('#> ')

                text = ""
                key = ""
                save_location = ""

                match choice:
                    case '1':
                        with open(config['encrypted-file-location'], 'rb') as r_file:
                            text = r_file.read().decode()
                        save_location = config['decrypted-file-location']
                        key = config['key']
                    case '2':
                        with open(input('Enter file location: '), 'rb') as r_file:
                            text = r_file.read().decode()
                        save_location = input('Enter save location: ')
                        key = input('Enter key: ')

                # Decrypt text
                decrypted_text = decrypt(text, key)
                # Save decrypted text
                f = open(save_location, 'w')
                f.write(decrypted_text)
                f.close()
            case '3':
                break
            case _: print('Invalid choice')


if __name__ == '__main__':
    main()
