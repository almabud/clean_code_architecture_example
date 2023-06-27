from enum import Enum


class RequestMethod(Enum):
    post = 'POST'
    get = 'GET'
    put = 'PUT'
    patch = 'PATCH'
    delete = 'DELETE'
