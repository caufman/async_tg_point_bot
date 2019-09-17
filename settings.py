from os import path as osp


BASE_DIR = osp.abspath(osp.dirname(__file__))
BASE_POINT_URL = r'http://point.im/api/'

with open(osp.join(BASE_DIR, 'bot.token'), mode="r", encoding='utf-8') as bt_file:
    BOT_TOKEN = bt_file.readline().strip()

