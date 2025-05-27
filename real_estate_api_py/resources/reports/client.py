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


class ReportsClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def property_liens(
        self,
        *,
        data: typing.Union[
            typing.Optional[params.ReportsPropertyLiensBody], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        Involuntary Liens API

        Go beyond our standard tax_liens & add Involuntary Lien Data to your Insights on a Property

        POST /v2/Reports/PropertyLiens

        Args:
            data: ReportsPropertyLiensBody
            request_options: Additional options to customize the HTTP request

        Returns:
            200

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.reports.property_liens()
        ```
        """
        _json = (
            to_encodable(
                item=data, dump_with=params._SerializerReportsPropertyLiensBody
            )
            if data
            else None
        )
        return self._base_client.request(
            method="POST",
            path="/v2/Reports/PropertyLiens",
            auth_names=["sec0"],
            json=_json,
            cast_to=typing.Dict[str, typing.Any],
            request_options=request_options or default_request_options(),
        )


class AsyncReportsClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def property_liens(
        self,
        *,
        data: typing.Union[
            typing.Optional[params.ReportsPropertyLiensBody], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        Involuntary Liens API

        Go beyond our standard tax_liens & add Involuntary Lien Data to your Insights on a Property

        POST /v2/Reports/PropertyLiens

        Args:
            data: ReportsPropertyLiensBody
            request_options: Additional options to customize the HTTP request

        Returns:
            200

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.reports.property_liens()
        ```
        """
        _json = (
            to_encodable(
                item=data, dump_with=params._SerializerReportsPropertyLiensBody
            )
            if data
            else None
        )
        return await self._base_client.request(
            method="POST",
            path="/v2/Reports/PropertyLiens",
            auth_names=["sec0"],
            json=_json,
            cast_to=typing.Dict[str, typing.Any],
            request_options=request_options or default_request_options(),
        )
