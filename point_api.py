from settings import BASE_POINT_URL

import asyncio
from aiohttp import ClientSession
import json


def join_url(left, right):
    if right[0] == '/':
        right = right[1:]
    delim = '/' if left[-1] != '/' else ''
    return f'{left}{delim}{right}'

def get_url(part):
    return join_url(BASE_POINT_URL, part)

async def login(username, password):
    async with ClientSession() as session:
        async with session.post(get_url('login'), data={
            'login': username,
            'password': password,
        }) as resp:
            login_data = json.loads(await resp.text())
            auth_token = login_data['token']
            csrf_token = login_data['csrf_token']
            print(f'Token: {auth_token}\n'
                f'CSRF Token: {csrf_token}')

if __name__ == '__main__':
    asyncio.run(login('cauf', 'c7h5n3o6'))
