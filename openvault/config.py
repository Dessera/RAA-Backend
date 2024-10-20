import os
from dotenv import dotenv_values


class __Config:
    database_url: str
    database_test_url: str
    app_base_url: str

    auth_secret_key: str
    auth_token_expire_minutes: int
    auth_algorithm: str

    def __init__(self):
        _cfg: dict[str, str | None] = {**dotenv_values(".env"), **os.environ}
        self.__check_database(_cfg)
        self.__check_app_base_url(_cfg)
        self.__check_auth(_cfg)

    def __check_database(self, _cfg: dict[str, str | None]):
        url = _cfg.get("DATABASE_URL")
        if url is None:
            raise ValueError("DATABASE_URL is not set")
        self.database_url = url

        test_url = _cfg.get("DATABASE_TEST_URL")
        if test_url is None:
            raise ValueError("DATABASE_TEST_URL is not set")
        self.database_test_url = test_url

    def __check_app_base_url(self, _cfg: dict[str, str | None]):
        url = _cfg.get("APP_BASE_URL")
        if url is None:
            raise ValueError("APP_BASE_URL is not set")
        self.app_base_url = url

    def __check_auth(self, _cfg: dict[str, str | None]):
        value = _cfg.get("AUTH_SECRET_KEY")
        if value is None:
            raise ValueError("AUTH_SECRET_KEY is not set")
        self.auth_secret_key = value

        value = _cfg.get("AUTH_TOKEN_EXPIRE_MINUTES")
        if value is None:
            raise ValueError("AUTH_TOKEN_EXPIRE_MINUTES is not set")
        self.auth_token_expire_minutes = int(value)

        value = _cfg.get("AUTH_ALGORITHM")
        if value is None:
            raise ValueError("AUTH_ALGORITHM is not set")
        self.auth_algorithm = value


CONFIG = __Config()
