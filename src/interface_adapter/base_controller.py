import functools

from pydantic import ValidationError

from src.core.entities.response import Response
from src.core.exceptions.exceptions import UnHandleRequest, DefaultException
from src.interface_adapter.permission import AllowAny
from src.interface_adapter.request_handler import (
    RequestHandler, AuthenticationHandler
)


def process_request(func):
    @functools.wraps(func)
    def wrapper(self, *args, **kwargs):
        # Process all request through the request processing pipeline.
        try:
            for handler in self.request_handler:
                res = handler(self.request).process_request()
                if res:
                    self.request = res
        except UnHandleRequest as e:
            return Response(status='error', error={'msg': e}, status_code=400)

        # Process all permissions.
        for permission in self.permissions:
            if not permission(self.request).has_permission():
                return Response(
                    status='error',
                    error={'msg': 'Permission denied.'},
                    status_code=401
                )
        try:
            return func(self, *args, **kwargs)
        except ValidationError as e:
            return Response(status='error', error=e.errors(), status_code=400)
        except DefaultException as e:
            return Response(
                status='error', error={'msg': e}, status_code=404
            )

    return wrapper


class ControllerMeta(type):
    def __new__(cls, name, bases, attrs):
        attrs['dispatch'] = process_request(attrs['dispatch'])

        return super().__new__(cls, name, bases, attrs)


class BaseController(metaclass=ControllerMeta):
    request_handler = (RequestHandler, AuthenticationHandler)
    permissions = (AllowAny,)

    def __init__(self, request):
        self.request = request

    def dispatch(self):
        raise NotImplementedError
