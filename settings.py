from os import path as osp
from configparser import ConfigParser


BASE_DIR = osp.abspath(osp.dirname(__file__))
BASE_POINT_URL = r'http://point.im/api/'

PSWD = ConfigParser()
PSWD.read(osp.join(BASE_DIR,'pswd.ini'))

BOT_TOKEN = PSWD['Tokens']['telegrambot']

DATABASE = {
    'role': 'tgbot',
    'password': PSWD['Passwords']['postgresql'],
}
