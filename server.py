import logging

from http.server import BaseHTTPRequestHandler
from routes.main import get_routes

logging.basicConfig(
    level=logging.DEBUG,
    filename='/var/log/cloud_monitoring_api.log',
    format='%(asctime)s - %(name)s - %(levelname)s: %(message)s'
)

logger = logging.getLogger("server.py")


class Server(BaseHTTPRequestHandler):

    def do_HEAD(self):
        return

    def do_POST(self):
        return

    def do_GET(self):
        self.respond("GET")

    def handle_http(self, method, status, content_type):
        self.send_response(status)
        self.send_header("Content-type", content_type)
        self.end_headers()

        route_content = None
        if method == "GET":
            route_content = self.__parse_route(get_routes, self.path)
        else:
            route_content = self.__parse_route(get_routes, self.path)

        logger.info("\"{method} {url}\" {status} {referrer}".format(
            method=method,
            url=self.path,
            status=status,
            referrer=self.client_address[0]
        ))
        return bytes(route_content, "UTF-8")

    def respond(self, method="GET"):
        content = self.handle_http(method, 200, "application/json")
        self.wfile.write(content)

    def __parse_route(self, routes, path):
        # if path not found on exist routes
        route = routes['/']
        if path in routes.keys():
            route = routes[path]
        return route
