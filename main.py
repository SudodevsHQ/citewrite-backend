import tornado.websocket
import tornado.ioloop
import tornado.web
from modules.EntityGen import Generator

import json

class EchoWebSocket(tornado.websocket.WebSocketHandler):
    def open(self):
        print("WebSocket opened")

    def on_message(self, message):
        g = Generator("1947 india got freedom yaas bitches")
        g.run()
        g.results()
        print(g.res)
        self.write_message(g.res)
        

    def on_close(self):
        print("WebSocket closed")

    def check_origin(self, origin):
        return True

def make_app():
    return tornado.web.Application([
        (r"/socket", EchoWebSocket)
    ])



if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()

