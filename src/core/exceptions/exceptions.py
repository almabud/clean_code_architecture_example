class DefaultException(Exception):
    pass


class InvalidToken(DefaultException):
    def __init__(self, message="Provided token is invalid"):
        self.message = message
        super().__init__(self.message)


class ExpiredToken(InvalidToken):
    def __init__(self, message="Token has expired."):
        self.message = message
        super().__init__(self.message)


class NotFound(DefaultException):
    def __init__(self, message="not found."):
        self.message = message
        super().__init__(self.message)


class UnHandleRequest(DefaultException):
    def __init__(self, message="can't process the request."):
        self.message = message
        super().__init__(self.message)


class AuthenticationError(DefaultException):
    def __init__(self, message="Invalid email and password."):
        self.message = message
        super().__init__(self.message)
