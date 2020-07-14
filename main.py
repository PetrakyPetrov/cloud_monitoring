#!/usr/bin/env python3
import time
import os
import logging

from http.server import HTTPServer
from server import Server

logging.basicConfig(
    level=logging.DEBUG,
    filename='/var/log/cloud_monitoring_api.log',
    format='%(asctime)s - %(name)s - %(levelname)s: %(message)s'
)

logger = logging.getLogger(__file__)

HOST_NAME = os.environ.get('HOST_API_URL', "localhost")
PORT = os.environ.get('HOST_API_PORT', 4501)

if __name__ == '__main__':

    httpd = HTTPServer((HOST_NAME, PORT), Server)
    logger.info("Server UP {host_name}:{port}".format(
        host_name=HOST_NAME,
        port=PORT
    ))

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        logger.error("Server stoped")
        pass

    httpd.server_close()
    logger.info("Server DOWN {host_name}:{port}".format(
        host_name=HOST_NAME,
        port=PORT
    ))
