import sys
import orm,asyncio
from models import User,Blog,Comment

@asyncio.coroutine
def test( loop ):
    yield from orm.create_pool( loop = loop, user = 'root', password = 'wzh12346578', db='test' )
    u = User(name = 'test11',email = 'test11@test.com',passwd = 'test',image = 'about:blank')
    yield from u.save()

if __name__ == '__main__':

    loop = asyncio.get_event_loop()
    loop.run_until_complete( asyncio.wait([test( loop )]) )
    loop.close()
    if loop.is_closed():
        sys.exit(0)

