import configparser

config = configparser.ConfigParser()
config["DEFAULT"] = {'ServerAliveInterval': '45',
                      'Compression': 'yes',
                     'CompressionLevel': '9'}

config['bitbucket'] = {}
config['bitbucket']['User'] = 'hou'

config['topsecret.server.com'] = {}
topsecret = config['topsecret.server.com']
topsecret['Host Port'] = '50022'
topsecret['ForwardX11'] = 'no'
config['DEFAULT']['ForwardX11'] = 'yes'

with open('example.ini', 'w') as configfile:
   config.write(configfile)

config.read('example.ini')
print(config.sections())