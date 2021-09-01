from configparser import ConfigParser


# parse config
config = ConfigParser()
config.read('config.ini')

# project section
DEBUG = config.get('project', 'debug')

# bot section
TOKEN = config.get('bot', 'token')
ADMINS = tuple(map(int, config.get('bot', 'admins').split(',')))
DEVELOPER = config.getint('bot', 'developer')

# database section
SQLITE_PATH = config.get('database', 'sqlite')

# server section
LISTEN = config.get('server', 'listen')
HOST = config.get('server', 'host')
PORT = config.getint('server', 'port')

# webhook section
WEBHOOK_URL = config.get('webhook', 'webhook_url')
PKEY_PATH = config.get('webhook', 'Pkey_path')
CERT_PATH = config.get('webhook', 'cert_path')
