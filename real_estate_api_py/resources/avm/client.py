import typing

from real_estate_api_py.core import (
    AsyncBaseClient,
    RequestOptions,
    SyncBaseClient,
    default_request_options,
    to_encodable,
    type_utils,
)
from real_estate_api_py.types import models, params


class AvmClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def get_valuation(
        self,
        *,
        address: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        id: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        strict: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.AvmGetValuationResponse:
        """
        Lender Grade AVM API

        Get the most precise property valuations using our lender-grade Automated Valuation Model
        that uses statistical modeling, recent sales data, and market-to-market analysis.


        POST /v2/PropertyAvm

        Args:
            address: Fully formatted address
            id: Property ID from search results
            strict: Enable strict address matching
            request_options: Additional options to customize the HTTP request

        Returns:
            Property valuation retrieved successfully

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.avm.get_valuation(address="123 Main St, Arlington, VA 22205")
        ```
        """
        _json = to_encodable(
            item={"address": address, "id": id, "strict": strict},
            dump_with=params._SerializerAvmGetValuationBody,
        )
        return self._base_client.request(
            method="POST",
            path="/v2/PropertyAvm",
            auth_names=["ApiKeyAuth"],
            json=_json,
            cast_to=models.AvmGetValuationResponse,
            request_options=request_options or default_request_options(),
        )


class AsyncAvmClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def get_valuation(
        self,
        *,
        address: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        id: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        strict: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.AvmGetValuationResponse:
        """
        Lender Grade AVM API

        Get the most precise property valuations using our lender-grade Automated Valuation Model
        that uses statistical modeling, recent sales data, and market-to-market analysis.


        POST /v2/PropertyAvm

        Args:
            address: Fully formatted address
            id: Property ID from search results
            strict: Enable strict address matching
            request_options: Additional options to customize the HTTP request

        Returns:
            Property valuation retrieved successfully

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.avm.get_valuation(address="123 Main St, Arlington, VA 22205")
        ```
        """
        _json = to_encodable(
            item={"address": address, "id": id, "strict": strict},
            dump_with=params._SerializerAvmGetValuationBody,
        )
        return await self._base_client.request(
            method="POST",
            path="/v2/PropertyAvm",
            auth_names=["ApiKeyAuth"],
            json=_json,
            cast_to=models.AvmGetValuationResponse,
            request_options=request_options or default_request_options(),
        )
