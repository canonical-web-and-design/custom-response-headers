# canonicalwebteam.custom-response-headers

Django middleware for setting custom HTTP haders to be included in every HTTP response.

## Installation

`custom-response-headers` can be installed direct from PyPi:

``` bash
pip install canonicalwebteam.middleware.custom-response-headers
```

## Usage

To enable the middleware, update your `{app}/settings.py` to add the module to `MIDDLEWARE` and define a `CUSTOM_HEADERS` dictionary as follows:

``` python
MIDDLEWARE = ['canonicalwebteam.custom_response_headers.Middleware']
# ...
CUSTOM_HEADERS = {'X-Custom-Header': 'Some custom value'}
```

Now the `X-Custom-Header` HTTP header will be added to every response, e.g.:

``` bash
$ curl -I http://127.0.0.1:8000
HTTP/1.0 200 OK
X-Custom-Header: Some custom value
```

