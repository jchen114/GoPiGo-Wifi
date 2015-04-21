__author__ = 'Kingpin'
from GPGSocketClient.KeyboardInput import DetectEvent as de
from ws4py.client.threadedclient import WebSocketClient


class SomeClient(WebSocketClient):

    def opened(self):
        self.send('Hello')

    def closed(self, code, reason=None):
        print "Closed down", code, reason

    def received_message(self, message):
        print message


class KeyboardHandler:

    socketCli = None

    def __init__(self, socket_client):
        self.socketCli = socket_client
        self.keyboardDetector = de.KeyboardDetector(self)

    def key_pressed(self, event):
        if event.char == 'w':
            print 'UP'
            self.socketCli.send('UP')
        elif event.char == 's':
            print 'DOWN'
            self.socketCli.send('DOWN')
        elif event.char == 'a':
            print 'LEFT'
            self.socketCli.send('LEFT')
        elif event.char == 'd':
            print 'RIGHT'
            self.socketCli.send('RIGHT')
        #print 'Delegate got %s\n' % (event.char, )


if __name__ == "__main__":
    ws = SomeClient('ws://localhost:8888/echo', protocols=['http-only', 'chat'])
    try:
        ws.connect()
        KeyboardHandler(ws)
    except KeyboardInterrupt:
        ws.close()


