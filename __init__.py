import pprint

class LoggingMiddleware:
    def __init__(self, application):
        self.__application = application

    def __call__(self, environ, start_response):
        errors = environ['wsgi.errors']
        pprint.pprint(('REQUEST', environ), stream=errors)

        def _start_response(status, headers):
            pprint.pprint(('RESPONSE', status, headers), stream=errors)
            return start_response(status, headers)

        return self.__application(environ, _start_response)
