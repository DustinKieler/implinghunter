import configparser


def create_config():
    config = configparser.ConfigParser()
    config['CREDENTIALS'] = {'Address': 'YOUR GMAIL ADDRESS HERE',
                             'Key': 'THE PASSWORD TO YOUR GMAIL ADDRESS HERE'}
    with open('auth.ini', 'w') as output_file:
        config.write(output_file)
