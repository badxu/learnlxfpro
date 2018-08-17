import logging; logging.basicConfig(level=logging.INFO)

import asyncio, os, json, time
from datetime import datetime

from aiohttp import web

def index(request):
    return web.Response(body=b'<h1>Awesome</h1>',content_type='text/html')

@asyncio.coroutine
async def init(event_loop):
    #创建web服务器实例
    app = web.Application(loop=event_loop)
    app.router.add_route('GET', '/', index)
    #利用event_loop.creat_server()创建TCP服务
    app_runner = web.AppRunner(app)
    srv = await event_loop.create_server(app_runner.app.make_handler(), '127.0.0.1', 9000)
    logging.info('server started at http://127.0.0.1:9000...')

    rs = dict()
    rs['app'] = app
    rs['srv'] = srv
    rs['handler'] = handler
    return rs
    return 

loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()