from os import path as osp
from configparser import ConfigParser

BASE_DIR = osp.abspath(osp.dirname(__file__))

TOKENS_PATH = osp.join(BASE_DIR, "tokens.ini")
TOKENS = ConfigParser()
TOKENS.read(TOKENS_PATH)

BOT_TOKEN = TOKENS['API_Token']['Telegram_Bot']

