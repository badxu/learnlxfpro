import logging; logging.basicConfig(level=logging.INFO)

import asyncio, orm,os, json, time
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
    handler = app_runner.app.make_handler()
    srv = await event_loop.create_server(handler, '127.0.0.1', 9000)
    logging.info('server started at http://127.0.0.1:9000...')
    #modify by badxu for resolve dbaccess_test --loop is closed---
    rs = dict()
    rs['app'] = app
    rs['srv'] = srv
    rs['handler'] = handler
    return rs
    ############
    #return srv
    app.on_shutdown.append(on_close)

loop = asyncio.get_event_loop()
rs = loop.run_until_complete(init(loop))
try:
    loop.run_forever()
except KeyboardInterrupt:
    pass
finally:
    rs['srv'].close()
    loop.run_until_complete(rs['srv'].wait_closed())
    loop.run_until_complete(rs['app'].shutdown())
    loop.run_until_complete(rs['handler'].finish_connections(60.0))
    loop.run_until_complete(rs['app'].cleanup())
loop.close()

async def on_close(app):
    await orm.close_pool()

