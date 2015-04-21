__author__ = 'Kingpin'
from tornado import websocket, web, ioloop


class SocketHandler(websocket.WebSocketHandler):

    def check_origin(self, origin):
        return True

    def on_message(self, message):
        self.write_message(u"You said: " + message)

    def open(self):
        self.write_message(u"Hello")

    def on_close(self):
        print 'Closed'

app = web.Application([
    (r'/echo', SocketHandler),
])

if __name__ == "__main__":
    app.listen(8888)
    ioloop.IOLoop.instance().start()