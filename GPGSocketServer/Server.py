__author__ = 'Kingpin'
from tornado import websocket, web, ioloop
from Manager import GPGManager


class EchoSocketHandler(websocket.WebSocketHandler):

    def check_origin(self, origin):
        return True

    def on_message(self, message):
        self.write_message(u"You said: " + message)

    def open(self):
        self.write_message(u"Hello")

    def on_close(self):
        print 'Closed'


class GPGSocketHandler(websocket.WebSocketHandler):

    gpgM = None    

    def check_origin(self, origin):
        return True

    def on_message(self, message):
        print "Received: " + message
        if message == 'UP':
            print 'fwd()'
            self.gpgM.go_forward()
        if message == 'DOWN':
            print 'bwd()'
            self.gpgM.go_backward()
        if message == 'LEFT':
            print 'left()'
            self.gpgM.turn_left()
        if message == 'RIGHT':
            print 'right()'
            self.gpgM.turn_right()
        if message == 'STOP':
            print 'stop()'
            self.gpgM.stop()

    def open(self):
        self.gpgM = GPGManager()
        self.write_message(u"Hello")

    def on_close(self):
        print 'Closed'


app = web.Application([
    (r'/echo', EchoSocketHandler),
    (r'/gpg', GPGSocketHandler)
])

if __name__ == "__main__":
    # Create instance of Manager.
    app.listen(8888)
    ioloop.IOLoop.instance().start()
