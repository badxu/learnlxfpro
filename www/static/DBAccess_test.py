import orm,asyncio
from models import User, Blog, Comment

@asyncio.coroutine
def test():
    yield from orm.create_pool(loop = loop,user='root', password='wzh12346578', db='test')

    u = User(name='Test5', email='test5@example.com', passwd='1234567890', image='about:blank')

    yield from u.save()

loop = asyncio.get_event_loop()
loop.run_until_complete(test())
loop.close()

