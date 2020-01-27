from django.conf import settings
from django.utils.deprecation import MiddlewareMixin


class Middleware(MiddlewareMixin):
    def process_response(self, request, response):
        """
        Look for a "CUSTOM_HEADERS" dictionary
        and add any non-empty values from that dictionary
        as custom HTTP headers
        """

        custom_headers = getattr(settings, "CUSTOM_HEADERS", {})

        for header_name, header_value in custom_headers.items():
            if header_value not in [None, ""]:
                response[header_name] = header_value

        return response
