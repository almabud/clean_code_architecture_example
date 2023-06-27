from datetime import datetime, timedelta

import jwt
from jwt import InvalidTokenError, DecodeError, InvalidSignatureError, \
    ExpiredSignatureError

from src.config import config
from src.core.entities.token import Token
from src.core.exceptions.exceptions import InvalidToken, ExpiredToken
from src.core.repositories.token_repo import TokenRepo


class JwtTokenRepo(TokenRepo):
    def generate_token(self, user) -> Token:
        encoded = jwt.encode(
            {
                "identifier": str(user.identifier),
                "exp":  datetime.utcnow() + timedelta(
                    seconds=config.TOKEN_EXPIRY
                )
            },
            config.SECRET_KEY,
            algorithm="HS256"
        )

        return self. build_entity_obj({'access_token': encoded})

    def verify_token(self, token: str):
        try:
            verify = jwt.decode(token, config.SECRET_KEY, algorithms="HS256")
            return self.build_entity_obj(
                {'access_token': token, 'payload': verify}
            )
        except (InvalidTokenError, DecodeError, InvalidSignatureError):
            raise InvalidToken
        except ExpiredSignatureError:
            raise ExpiredToken

    def build_entity_obj(self, data):
        return Token(**data)
