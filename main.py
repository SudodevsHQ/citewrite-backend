import tornado.websocket
import tornado.ioloop
import tornado.web
from tornado import gen
from modules.EntityGen import Generator
from modules.RawResponse import RawGenerator

import json


class NlpWebSocket(tornado.websocket.WebSocketHandler):
    def open(self):
        print("WebSocket opened")

    @gen.coroutine
    def on_message(self, message):
        g = Generator(message)
        g.run()
        g.results()
        print(g.res)
        self.write_message(g.res)

    @gen.coroutine
    def on_close(self):
        print("WebSocket closed")

    @gen.coroutine
    def check_origin(self, origin):
        return True


class RawWbeSocket(tornado.websocket.WebSocketHandler):
    def open(self):
        print("WebSocket opened")

    @gen.coroutine
    def on_message(self, message):
        g = RawGenerator(message)
        g.results()
        print(g.res)
        self.write_message(g.res)

    @gen.coroutine
    def on_close(self):
        print("WebSocket closed")

    @gen.coroutine
    def check_origin(self, origin):
        return True


def make_app():
    return tornado.web.Application([
        (r"/socket/nlp", NlpWebSocket),
        (r"/socket/raw", RawWbeSocket)

    ], debug=True, autoreload=True)


if __name__ == "__main__":
    port = 5876
    app = make_app()
    app.listen(port)
    print("started webserver at port " + str(port))
    tornado.ioloop.IOLoop.current().start()
