#!/usr/bin/env python3
import time
import os

from http.server import HTTPServer
from server import Server

HOST_NAME = os.environ.get('HOST_API_URL', "localhost")
PORT_NUMBER = os.environ.get('HOST_API_PORT', 8000)

if __name__ == '__main__':

    httpd = HTTPServer((HOST_NAME, PORT_NUMBER), Server)
    print(time.asctime(), 'Server UP - %s:%s' % (HOST_NAME, PORT_NUMBER))

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass

    httpd.server_close()
    print(time.asctime(), 'Server DOWN - %s:%s' % (HOST_NAME, PORT_NUMBER))