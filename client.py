import socket, videosocket
import StringIO
from videofeed import VideoFeed
import sys

class Client:
    def __init__(self, ip_addr = "127.0.0.1"):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect((ip_addr, 6000))
        self.vsock = videosocket.videosocket (self.client_socket)
        self.videofeed = VideoFeed(1,"client",1)
        self.data = StringIO.StringIO()

    def connect(self):
        while True:
            frame=self.videofeed.get_frame()
            self.vsock.vsend(frame)
            frame = self.vsock.vreceive()
            self.videofeed.set_frame(frame)

if __name__ == "__main__":
    ip_addr = "127.0.0.1"
    if len(sys.argv) == 2:
        ip_addr = sys.argv[1]

    print "Connecting to " + ip_addr + "...."
    client = Client(ip_addr)
    client.connect()
