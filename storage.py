import settings

import asyncio
import psycopg2 as pg

connect_string = f'dbname={settings.DATABASE["database"]} user={settings.DATABASE["role"]} password={settings.DATABASE["password"]} host={settings.DATABASE["host"]} port={settings.DATABASE["port"]}'

async def create_auth_table():
    cur.execute('''
        CREATE TABLE IF NOT EXISTS auth_user (
            id SERIAL PRIMARY KEY,
            tg_username VARCHAR(255) UNIQUE NOT NULL,
            tg_userid VARCHAR(255) UNIQUE NOT NULL,
            point_username VARCHAR(255),
            API_token VARCHAR(255),
            CSRF_token VARCHAR(255)
        )
                      ''')
    print(f'Создана таблица "auth_user".')


async def run_func(func, args=None, kwargs=None):
    loop.run_until_complete(func(*args, **kwargs))





conn = pg.connect(connect_string)
cur = conn.cursor()
loop = asyncio.get_event_loop()
loop.run_until_complete(create_auth_table())
