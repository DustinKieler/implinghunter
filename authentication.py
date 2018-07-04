'''
This script creates an 'auth.ini' folder which will be created when create_config() runs.
The 'auth.ini' file will be read when an e-mail needs to be sent to a user, it contains the gmail
address and password of the user to send the e-mail to so the credentials are not hard-coded in.
'''

import configparser


def create_config():
    """Creates a file named 'auth.ini' which holds the email recipient's gmail authentication credentials listed here.
	   These will be read when an e-mail is created and sent."""
    config = configparser.ConfigParser()
    config['CREDENTIALS'] = {'Address': 'YOUR GMAIL ADDRESS HERE',
                             'Key': 'THE PASSWORD TO YOUR GMAIL ADDRESS HERE'}
    with open('auth.ini', 'w') as output_file:
        config.write(output_file)
