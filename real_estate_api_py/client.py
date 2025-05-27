import httpx
import typing

from real_estate_api_py.core import AsyncBaseClient, AuthKeyHeader, SyncBaseClient
from real_estate_api_py.environment import Environment, _get_base_url
from real_estate_api_py.resources.address import AddressClient, AsyncAddressClient
from real_estate_api_py.resources.gpt import AsyncGptClient, GptClient
from real_estate_api_py.resources.property import AsyncPropertyClient, PropertyClient
from real_estate_api_py.resources.reports import AsyncReportsClient, ReportsClient
from real_estate_api_py.resources.valuation import AsyncValuationClient, ValuationClient


class Client:
    def __init__(
        self,
        *,
        timeout: typing.Optional[float] = 60,
        httpx_client: typing.Optional[httpx.Client] = None,
        base_url: typing.Optional[str] = None,
        environment: Environment = Environment.PRODUCTION,
        api_key: typing.Optional[str] = None,
    ):
        """Initialize root client"""
        self._base_client = SyncBaseClient(
            base_url=_get_base_url(base_url=base_url, environment=environment),
            httpx_client=httpx.Client(timeout=timeout)
            if httpx_client is None
            else httpx_client,
        )
        self._base_client.register_auth(
            "sec0", AuthKeyHeader(header_name="x-api-key", val=api_key)
        )
        self.address = AddressClient(base_client=self._base_client)
        self.property = PropertyClient(base_client=self._base_client)
        self.gpt = GptClient(base_client=self._base_client)
        self.valuation = ValuationClient(base_client=self._base_client)
        self.reports = ReportsClient(base_client=self._base_client)


class AsyncClient:
    def __init__(
        self,
        *,
        timeout: typing.Optional[float] = 60,
        httpx_client: typing.Optional[httpx.AsyncClient] = None,
        base_url: typing.Optional[str] = None,
        environment: Environment = Environment.PRODUCTION,
        api_key: typing.Optional[str] = None,
    ):
        """Initialize root client"""
        self._base_client = AsyncBaseClient(
            base_url=_get_base_url(base_url=base_url, environment=environment),
            httpx_client=httpx.AsyncClient(timeout=timeout)
            if httpx_client is None
            else httpx_client,
        )
        self._base_client.register_auth(
            "sec0", AuthKeyHeader(header_name="x-api-key", val=api_key)
        )
        self.address = AsyncAddressClient(base_client=self._base_client)
        self.property = AsyncPropertyClient(base_client=self._base_client)
        self.gpt = AsyncGptClient(base_client=self._base_client)
        self.valuation = AsyncValuationClient(base_client=self._base_client)
        self.reports = AsyncReportsClient(base_client=self._base_client)
