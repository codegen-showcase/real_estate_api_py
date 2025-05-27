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


class AddressClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def verify(
        self,
        *,
        data: typing.Union[
            typing.Optional[params.AddressVerifyBody], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Union[
        models.AddressVerifyResponseObj0, models.AddressVerifyResponseObj1
    ]:
        """
        Address Verification API

        Verify 1 - 100 addresses at a time.

        POST /v2/AddressVerification

        Args:
            data: AddressVerifyBody
            request_options: Additional options to customize the HTTP request

        Returns:
            200

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.address.verify()
        ```
        """
        _json = (
            to_encodable(item=data, dump_with=params._SerializerAddressVerifyBody)
            if data
            else None
        )
        return self._base_client.request(
            method="POST",
            path="/v2/AddressVerification",
            auth_names=["sec0"],
            json=_json,
            cast_to=typing.Union[
                models.AddressVerifyResponseObj0, models.AddressVerifyResponseObj1
            ],
            request_options=request_options or default_request_options(),
        )


class AsyncAddressClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def verify(
        self,
        *,
        data: typing.Union[
            typing.Optional[params.AddressVerifyBody], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Union[
        models.AddressVerifyResponseObj0, models.AddressVerifyResponseObj1
    ]:
        """
        Address Verification API

        Verify 1 - 100 addresses at a time.

        POST /v2/AddressVerification

        Args:
            data: AddressVerifyBody
            request_options: Additional options to customize the HTTP request

        Returns:
            200

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.address.verify()
        ```
        """
        _json = (
            to_encodable(item=data, dump_with=params._SerializerAddressVerifyBody)
            if data
            else None
        )
        return await self._base_client.request(
            method="POST",
            path="/v2/AddressVerification",
            auth_names=["sec0"],
            json=_json,
            cast_to=typing.Union[
                models.AddressVerifyResponseObj0, models.AddressVerifyResponseObj1
            ],
            request_options=request_options or default_request_options(),
        )
