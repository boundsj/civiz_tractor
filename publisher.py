import os, urlparse
import redis

class Publisher(object):

    def __init__(self):
        urlparse.uses_netloc.append('redis')
        url = urlparse.urlparse(os.environ['REDISTOGO_URL'])
        self.r = redis.Redis(host=url.hostname, port=url.port, db=0, password=url.password)

    def publish(self, document):
        self.r.publish('tweets', document)
