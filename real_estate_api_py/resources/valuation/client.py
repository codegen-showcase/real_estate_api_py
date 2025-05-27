import typing

from real_estate_api_py.core import (
    AsyncBaseClient,
    RequestOptions,
    SyncBaseClient,
    default_request_options,
    to_encodable,
    type_utils,
)
from real_estate_api_py.types import params


class ValuationClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def avm(
        self,
        *,
        data: typing.Union[
            typing.Optional[params.ValuationAvmBody], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        Lender Grade AVM API

        Need the most precise Valuations for properties possible? Try out our Lender Grade AVM that uses statistical modeling, recent sales data, and market-to-market analysis to produce reliable AVMs

        POST /v2/PropertyAvm

        Args:
            data: ValuationAvmBody
            request_options: Additional options to customize the HTTP request

        Returns:
            200

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.valuation.avm()
        ```
        """
        _json = (
            to_encodable(item=data, dump_with=params._SerializerValuationAvmBody)
            if data
            else None
        )
        return self._base_client.request(
            method="POST",
            path="/v2/PropertyAvm",
            auth_names=["sec0"],
            json=_json,
            cast_to=typing.Dict[str, typing.Any],
            request_options=request_options or default_request_options(),
        )


class AsyncValuationClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def avm(
        self,
        *,
        data: typing.Union[
            typing.Optional[params.ValuationAvmBody], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        Lender Grade AVM API

        Need the most precise Valuations for properties possible? Try out our Lender Grade AVM that uses statistical modeling, recent sales data, and market-to-market analysis to produce reliable AVMs

        POST /v2/PropertyAvm

        Args:
            data: ValuationAvmBody
            request_options: Additional options to customize the HTTP request

        Returns:
            200

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.valuation.avm()
        ```
        """
        _json = (
            to_encodable(item=data, dump_with=params._SerializerValuationAvmBody)
            if data
            else None
        )
        return await self._base_client.request(
            method="POST",
            path="/v2/PropertyAvm",
            auth_names=["sec0"],
            json=_json,
            cast_to=typing.Dict[str, typing.Any],
            request_options=request_options or default_request_options(),
        )
