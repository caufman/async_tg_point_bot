from os import path as osp
from configparser import ConfigParser

BASE_DIR = osp.abspath(osp.dirname(__file__))
BASE_POINT_URL = r'http://point.im/api/'

TOKENS_PATH = osp.join(BASE_DIR, "tokens.ini")
TOKENS = ConfigParser()
TOKENS.read(TOKENS_PATH)

BOT_TOKEN = TOKENS['API_Tokens']['telegrambot']

DATABASE = {
    'role': 'tgbot',
    'password': TOKENS['Passwords']['postgresql'],
    'database': 'tgpointbot',
    'host': '127.0.0.1',
    'port': '7070',
}
