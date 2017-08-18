from django.conf import settings

class Middleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        custom_headers = getattr(settings, 'CUSTOM_HEADERS', {})

        for header_name, header_value in custom_headers.items():
            if header_value not in [None, ""]:
                response[header_name] = header_value

        return response

