"""The one error hierarchy.

Every error the SDK raises is a :class:`TawkedError`. An answer of the API is an :class:`APIError`
subclass chosen by the documented status of its ``code`` (falling back to the HTTP status for an
undocumented code). ``message`` is the API's own; the request id is in every error's string form.
No key, token, client secret, webhook secret or ``Authorization`` header ever reaches an error.
"""

from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from tawked._transport import PreparedRequest

__all__ = [
    "APIConnectionError",
    "APIError",
    "APITimeoutError",
    "ApprovalRequiredError",
    "AuthenticationError",
    "BadRequestError",
    "ConflictError",
    "GoneError",
    "IdempotencyError",
    "InsufficientCreditsError",
    "InsufficientScopeError",
    "InternalServerError",
    "NotFoundError",
    "OAuthError",
    "PermissionDeniedError",
    "RateLimitError",
    "SecretNotReplayableError",
    "TawkedError",
    "UnexpectedResponseError",
    "UnprocessableEntityError",
    "WebhookVerificationError",
]


class TawkedError(Exception):
    """The base of every error this package raises."""


class APIConnectionError(TawkedError):
    """The API could not be reached, or the connection broke (network, DNS, TLS).

    ``idempotency_key`` is set when the request may have reached the server: call again with that
    key (never a new one) to retry safely.
    """

    def __init__(
        self,
        message: str,
        *,
        idempotency_key: str | None = None,
        sent: bool = False,
    ) -> None:
        super().__init__(message)
        self.message = message
        self.idempotency_key = idempotency_key
        self.sent = sent


class APITimeoutError(APIConnectionError):
    """One attempt took longer than its timeout."""


class APIError(TawkedError):
    """An error answer of the API (any status but 2xx)."""

    status: int
    code: str
    message: str
    request_id: str | None
    body: Any
    headers: dict[str, str]
    fields: Any
    field_errors: Any
    retry_after: float | None
    idempotency_key: str | None
    required_scope: str | None
    used_by: list[str] | None
    resource_status: str | None
    next: str | None
    human_action: Any
    approval: Any
    did_you_mean: Any
    #: Set on an after-send failure: what to do so the request is not applied twice.
    advice: str | None = None

    def __init__(
        self,
        message: str,
        *,
        status: int,
        code: str,
        request_id: str | None = None,
        body: Any = None,
        headers: Mapping[str, str] | None = None,
        retry_after: float | None = None,
        idempotency_key: str | None = None,
        required_scope: str | None = None,
    ) -> None:
        self.status = status
        self.code = code
        self.message = message
        self.request_id = request_id
        self.body = body
        self.headers = {
            k.lower(): v for k, v in (headers or {}).items() if k.lower() != "authorization"
        }
        self.retry_after = retry_after
        self.idempotency_key = idempotency_key
        self.required_scope = required_scope
        data = body if isinstance(body, dict) else {}
        fields = data.get("fields")
        self.fields = fields
        self.field_errors = (
            data.get("errors")
            if "errors" in data
            else (fields if isinstance(fields, dict) else None)
        )
        used_by = data.get("used_by")
        self.used_by = [str(u) for u in used_by] if isinstance(used_by, list) else None
        status_value = data.get("status")
        self.resource_status = status_value if isinstance(status_value, str) else None
        self.next = data.get("next") if isinstance(data.get("next"), str) else None
        self.human_action = data.get("human_action")
        self.approval = data.get("approval")
        self.did_you_mean = data.get("did_you_mean")
        super().__init__(self._render())

    def _render(self) -> str:
        text = f"{self.status} {self.code}"
        if self.message and self.message != self.code:
            text += f": {self.message}"
        if self.request_id:
            text += f" (request {self.request_id})"
        return text

    def __repr__(self) -> str:
        return f"{type(self).__name__}(status={self.status!r}, code={self.code!r}, request_id={self.request_id!r})"


class BadRequestError(APIError):
    """400."""


class AuthenticationError(APIError):
    """401."""


class InsufficientCreditsError(APIError):
    """402."""


class PermissionDeniedError(APIError):
    """403."""


class InsufficientScopeError(PermissionDeniedError):
    """403 with ``WWW-Authenticate: Bearer error="insufficient_scope"``; ``required_scope`` names it."""


class NotFoundError(APIError):
    """404."""


class ConflictError(APIError):
    """409."""


class IdempotencyError(ConflictError):
    """409 ``idempotency_*``: the key was used for another request, or is still being processed."""


class SecretNotReplayableError(IdempotencyError):
    """409 ``idempotency_secret_not_replayable``: the first answer carried a secret, shown once.

    Find what it made by ``id``, then rotate or revoke it.
    """

    @property
    def id(self) -> str | None:
        data = self.body if isinstance(self.body, dict) else {}
        value = data.get("id")
        return str(value) if value is not None else None

    @property
    def original_status(self) -> int | None:
        data = self.body if isinstance(self.body, dict) else {}
        value = data.get("original_status")
        return int(value) if isinstance(value, int) else None


class GoneError(APIError):
    """410 (``product_retired``, an expired approval)."""


class UnprocessableEntityError(APIError):
    """422."""


class ApprovalRequiredError(APIError):
    """428 on the Account API: a person must approve this write first.

    Relay ``human_action`` to them, then ``account.approvals.wait_and_retry(error)`` sends the same
    request again, with the same ``Idempotency-Key`` and ``Tawked-Approval``, once it is approved.
    """

    request: PreparedRequest | None = None

    @property
    def approval_id(self) -> str | None:
        approval = self.approval
        if isinstance(approval, dict) and approval.get("id") is not None:
            return str(approval["id"])
        return None


class RateLimitError(APIError):
    """429. ``retry_after`` is the seconds the API asked to wait, when it said."""


class InternalServerError(APIError):
    """5xx."""


class UnexpectedResponseError(TawkedError):
    """A 2xx answer the SDK cannot read (not JSON)."""

    def __init__(
        self, message: str, *, status: int, request_id: str | None = None, body: Any = None
    ) -> None:
        super().__init__(
            f"{message} (status {status}" + (f", request {request_id})" if request_id else ")")
        )
        self.message = message
        self.status = status
        self.request_id = request_id
        self.body = body


class WebhookVerificationError(TawkedError):
    """A webhook failed verification. ``reason`` is one of ``missing_header``,
    ``no_secret_for_scheme``, ``timestamp_out_of_tolerance``, ``signature_mismatch``,
    ``malformed_header`` or ``malformed_body``."""

    def __init__(self, reason: str, message: str | None = None) -> None:
        super().__init__(message or reason)
        self.reason = reason


class OAuthError(TawkedError):
    """The connected apps' code exchange answered ``{error, error_description}``."""

    def __init__(
        self,
        error: str,
        description: str | None = None,
        *,
        status: int,
        request_id: str | None = None,
    ) -> None:
        text = f"{status} {error}" + (f": {description}" if description else "")
        if request_id:
            text += f" (request {request_id})"
        super().__init__(text)
        self.error = error
        self.code = error
        self.error_description = description
        self.status = status
        self.request_id = request_id


#: The role of each class, the shared role table's column (printed by ``scripts/error_roles.py``).
ROLES: dict[type[TawkedError], str] = {
    TawkedError: "base",
    APIConnectionError: "connection",
    APITimeoutError: "timeout",
    APIError: "api",
    BadRequestError: "bad_request",
    AuthenticationError: "authentication",
    InsufficientCreditsError: "credits",
    PermissionDeniedError: "permission",
    InsufficientScopeError: "scope",
    NotFoundError: "not_found",
    ConflictError: "conflict",
    IdempotencyError: "idempotency",
    SecretNotReplayableError: "secret_not_replayable",
    GoneError: "gone",
    UnprocessableEntityError: "unprocessable",
    ApprovalRequiredError: "approval",
    RateLimitError: "rate_limit",
    InternalServerError: "server",
    UnexpectedResponseError: "unexpected_response",
    WebhookVerificationError: "webhook",
    OAuthError: "oauth",
}

_BY_STATUS: dict[int, type[APIError]] = {
    400: BadRequestError,
    401: AuthenticationError,
    402: InsufficientCreditsError,
    403: PermissionDeniedError,
    404: NotFoundError,
    409: ConflictError,
    410: GoneError,
    422: UnprocessableEntityError,
    428: ApprovalRequiredError,
    429: RateLimitError,
}

#: The Account API's own refusal codes and their statuses (App\AccountApi\AccountApiErrors, Approvals).
ACCOUNT_ERROR_STATUS: dict[str, int] = {
    "invalid_request": 400,
    "invalid_json": 400,
    "unauthorized": 401,
    "insufficient_permission": 403,
    "forbidden": 403,
    "ip_not_allowed": 403,
    "account_suspended": 403,
    "no_console_access": 403,
    "setup_pending": 403,
    "approval_declined": 403,
    "not_found": 404,
    "approval_mismatch": 409,
    "approval_used": 409,
    "approval_stale": 409,
    "idempotency_key_reused": 409,
    "idempotency_in_progress": 409,
    "idempotency_secret_not_replayable": 409,
    "approval_expired": 410,
    "validation_failed": 422,
    "approval_required": 428,
    "rate_limited": 429,
    "internal_error": 500,
}


def error_class_for(
    code: str, status: int, documented: Mapping[str, int], www_authenticate: str | None = None
) -> type[APIError]:
    """The class for an error answer: by the code's documented status, else the HTTP status."""
    if code == "idempotency_secret_not_replayable":
        return SecretNotReplayableError
    if code.startswith("idempotency_"):
        return IdempotencyError
    if code == "insufficient_scope" or (
        www_authenticate and "insufficient_scope" in www_authenticate
    ):
        return InsufficientScopeError
    role_status = documented.get(code, status)
    if role_status >= 500:
        return InternalServerError
    return _BY_STATUS.get(role_status, InternalServerError if status >= 500 else APIError)


def role_of(cls: type[TawkedError]) -> str:
    for klass in cls.__mro__:
        if klass in ROLES:
            return ROLES[klass]
    return "base"
