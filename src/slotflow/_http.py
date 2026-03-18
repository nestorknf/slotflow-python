from __future__ import annotations

from typing import Any, Dict, Optional

import httpx

from ._errors import (
    AuthenticationError,
    ConflictError,
    NotFoundError,
    PaymentRequiredError,
    SlotflowError,
    ValidationError,
)

_DEFAULT_BASE_URL = "https://api.slotflow.dev"
_DEFAULT_TIMEOUT = 30.0

_ERROR_MAP = {
    401: AuthenticationError,
    402: PaymentRequiredError,
    404: NotFoundError,
    409: ConflictError,
    422: ValidationError,
}


def _raise_for_status(response: httpx.Response) -> None:
    if response.is_success:
        return
    try:
        body = response.json()
    except Exception:
        body = response.text
    cls = _ERROR_MAP.get(response.status_code, SlotflowError)
    raise cls(body)


class SyncHTTPClient:
    def __init__(
        self,
        api_key: str,
        base_url: Optional[str] = None,
        timeout: Optional[float] = None,
    ) -> None:
        self._client = httpx.Client(
            base_url=base_url or _DEFAULT_BASE_URL,
            headers={
                "Authorization": f"Bearer {api_key}",
                "Content-Type": "application/json",
                "User-Agent": "slotflow-python",
            },
            timeout=timeout or _DEFAULT_TIMEOUT,
        )

    def request(
        self,
        method: str,
        path: str,
        json: Optional[Dict[str, Any]] = None,
        params: Optional[Dict[str, Any]] = None,
    ) -> Any:
        # Filter None values from params
        if params:
            params = {k: v for k, v in params.items() if v is not None}
        response = self._client.request(method, path, json=json, params=params)
        _raise_for_status(response)
        if response.status_code == 204:
            return None
        return response.json()

    def close(self) -> None:
        self._client.close()


class AsyncHTTPClient:
    def __init__(
        self,
        api_key: str,
        base_url: Optional[str] = None,
        timeout: Optional[float] = None,
    ) -> None:
        self._client = httpx.AsyncClient(
            base_url=base_url or _DEFAULT_BASE_URL,
            headers={
                "Authorization": f"Bearer {api_key}",
                "Content-Type": "application/json",
                "User-Agent": "slotflow-python",
            },
            timeout=timeout or _DEFAULT_TIMEOUT,
        )

    async def request(
        self,
        method: str,
        path: str,
        json: Optional[Dict[str, Any]] = None,
        params: Optional[Dict[str, Any]] = None,
    ) -> Any:
        if params:
            params = {k: v for k, v in params.items() if v is not None}
        response = await self._client.request(method, path, json=json, params=params)
        _raise_for_status(response)
        if response.status_code == 204:
            return None
        return response.json()

    async def close(self) -> None:
        await self._client.aclose()
