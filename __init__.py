import logging

class LoggingMiddleware:
    def __init__(self, application, full=False):
        self._application = application
        self._full = full

    def __call__(self, environ, start_response):
        errors = environ['wsgi.errors']

        url = environ['wsgi.url_scheme'] + '://' + environ['HTTP_HOST'] + environ['PATH_INFO']
        if environ['QUERY_STRING']:
            url += '?' + environ['QUERY_STRING']
        request_method = environ['REQUEST_METHOD']
        logging.info(request_method + ' ' + url)

        if self._full:
            import pprint
            pprint.pprint(('REQUEST', environ), stream=errors)

            def _start_response(status, headers):
                pprint.pprint(('RESPONSE', status, headers), stream=errors)
                return start_response(status, headers)

            return self._application(environ, _start_response)
        else:
            return self._application(environ, start_response)
