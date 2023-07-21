from warmindo.core.request_manager import RequestManager
from warmindo.core.response import Response


class Router:
    def __init__(self):
        self.routes = []

    def route(self, path, methods=None):
        def decorator(handler):
            self.routes.append((path, methods, handler))
            return handler
        return decorator

    def resolve(self, request):
        for path, methods, handler in self.routes:
            if path == request.path and (methods is None or request.method in methods):
                return handler

class WarmindoApp:
    def __init__(self):
        self.router = Router()

    def add_route(self, path, methods=None):
        return self.router.route(path, methods)

    def handle_request(self, request):
        handler = self.router.resolve(request)
        if handler:
            return handler(request)
        else:
            return Response("Not Found", status=404)