import configparser
config = configparser.ConfigParser()
config['pyrogram'] = {'api_id': int(input('Enter your api_id: ')),
                     'api_hash': str(input('Enter your api_hash: '))}

with open('config.ini', 'w') as configfile:
   config.write(configfile)