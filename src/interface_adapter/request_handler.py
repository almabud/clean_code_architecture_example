from abc import ABC, abstractmethod

from src.core.entities.request import Request, AnonymousUser
from src.core.exceptions.exceptions import UnHandleRequest, DefaultException
from src.core.usecases.get_user import GetUserUseCase
from src.core.usecases.token_verify import TokenVerifyUseCase
from src.infrastructure.repositories.sqlalchemy.user_repo import UserRepo
from src.infrastructure.repositories.token_repo import JwtTokenRepo


class BaseRequestHandler(ABC):
    def __init__(self, request):
        self.request = request

    @abstractmethod
    def process_request(self):
        pass


class RequestHandler(BaseRequestHandler):
    def process_request(self):
        return Request(**self.request)


class AuthenticationHandler(BaseRequestHandler):
    def process_request(self):
        try:
            user_repo = UserRepo()
            token_repo = JwtTokenRepo()
            authorization = self.request.headers.get('Authorization')
            if not authorization:
                raise UnHandleRequest('Authorization header not provided.')
            # Extract the token from the Authorization header
            auth_type, token = authorization.split(' ')
            verify = TokenVerifyUseCase(token_repo, token).execute()
            user = GetUserUseCase(
                user_repo=user_repo, identifier=verify.payload.identifier
            ).execute()
            self.request.user = user
        except DefaultException as e:
            self.request.user = AnonymousUser()
