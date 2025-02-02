# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class AuthType(str, enum.Enum):
    """
    Enumeration of supported authentication types.

    Attributes:
    ----------
        oauth2: OAuth2 authentication.
        oauth2_with_refresh: OAuth2 authentication with refresh token.
        oauth2_with_refresh_rotating: OAuth2 authentication with rotating refresh token.
        trello_auth: Trello authentication.
        api_key: API key authentication.
        native_functionality: Native functionality.
        url_and_api_key: URL and API key authentication.
    """

    OAUTH_2 = "oauth2"
    OAUTH_2_WITH_REFRESH = "oauth2_with_refresh"
    OAUTH_2_WITH_REFRESH_ROTATING = "oauth2_with_refresh_rotating"
    TRELLO_AUTH = "trello_auth"
    API_KEY = "api_key"
    NATIVE_FUNCTIONALITY = "native_functionality"
    CONFIG_CLASS = "config_class"

    def visit(
        self,
        oauth_2: typing.Callable[[], T_Result],
        oauth_2_with_refresh: typing.Callable[[], T_Result],
        oauth_2_with_refresh_rotating: typing.Callable[[], T_Result],
        trello_auth: typing.Callable[[], T_Result],
        api_key: typing.Callable[[], T_Result],
        native_functionality: typing.Callable[[], T_Result],
        config_class: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is AuthType.OAUTH_2:
            return oauth_2()
        if self is AuthType.OAUTH_2_WITH_REFRESH:
            return oauth_2_with_refresh()
        if self is AuthType.OAUTH_2_WITH_REFRESH_ROTATING:
            return oauth_2_with_refresh_rotating()
        if self is AuthType.TRELLO_AUTH:
            return trello_auth()
        if self is AuthType.API_KEY:
            return api_key()
        if self is AuthType.NATIVE_FUNCTIONALITY:
            return native_functionality()
        if self is AuthType.CONFIG_CLASS:
            return config_class()
