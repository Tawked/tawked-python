"""The official Python SDK for Tawked (https://tawked.com).

    from tawked import Tawked

    tawked = Tawked()  # reads TAWKED_API_KEY
    sent = tawked.email.messages.send(
        from_="orders@acme.sa",
        to="sara@example.com",
        subject="Your order 1042",
        text="We are preparing it.",
        idempotency_key="order-1042-confirmation",
    )

``AsyncTawked`` is the async twin; ``TawkedAccount`` / ``AsyncTawkedAccount`` reach the Account API
with an account token; ``tawked.webhooks`` verifies the webhooks Tawked sends; ``tawked.apps``
connects your app to a merchant's application.
"""

from tawked import apps, error_codes, testing, webhooks
from tawked._client import AsyncTawked, Tawked
from tawked._envelope import AccountResponse
from tawked._errors import (
    APIConnectionError,
    APIError,
    APITimeoutError,
    ApprovalRequiredError,
    AuthenticationError,
    BadRequestError,
    ConflictError,
    GoneError,
    IdempotencyError,
    InsufficientCreditsError,
    InsufficientScopeError,
    InternalServerError,
    NotFoundError,
    OAuthError,
    PermissionDeniedError,
    RateLimitError,
    SecretNotReplayableError,
    TawkedError,
    UnexpectedResponseError,
    UnprocessableEntityError,
    WebhookVerificationError,
)
from tawked._generated.contract import API_VERSION, ErrorCode
from tawked._models import NOT_GIVEN, NotGiven, ResponseMeta
from tawked._pagination import AccountPage, Page
from tawked._version import __version__
from tawked.account import AsyncTawkedAccount, TawkedAccount
from tawked.attachments import attachment

VERSION = __version__

__all__ = [
    "API_VERSION",
    "NOT_GIVEN",
    "VERSION",
    "APIConnectionError",
    "APIError",
    "APITimeoutError",
    "AccountPage",
    "AccountResponse",
    "ApprovalRequiredError",
    "AsyncTawked",
    "AsyncTawkedAccount",
    "AuthenticationError",
    "BadRequestError",
    "ConflictError",
    "ErrorCode",
    "GoneError",
    "IdempotencyError",
    "InsufficientCreditsError",
    "InsufficientScopeError",
    "InternalServerError",
    "NotFoundError",
    "NotGiven",
    "OAuthError",
    "Page",
    "PermissionDeniedError",
    "RateLimitError",
    "ResponseMeta",
    "SecretNotReplayableError",
    "Tawked",
    "TawkedAccount",
    "TawkedError",
    "UnexpectedResponseError",
    "UnprocessableEntityError",
    "WebhookVerificationError",
    "__version__",
    "apps",
    "attachment",
    "error_codes",
    "testing",
    "webhooks",
]
