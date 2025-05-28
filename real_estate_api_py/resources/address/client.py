import typing
import typing_extensions

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
        addresses: typing.Union[
            typing.Optional[typing.List[params.AddressToVerify]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        strict: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.AddressVerifyResponse:
        """
        Address Verification API

        Verify 1 - 100 addresses at a time for accuracy and standardization.


        POST /v2/AddressVerification

        Args:
            addresses: typing.List[AddressToVerify]
            strict: Enable strict verification mode
            request_options: Additional options to customize the HTTP request

        Returns:
            Address verification results

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.address.verify()
        ```
        """
        _json = to_encodable(
            item={"addresses": addresses, "strict": strict},
            dump_with=params._SerializerAddressVerificationParameters,
        )
        return self._base_client.request(
            method="POST",
            path="/v2/AddressVerification",
            auth_names=["ApiKeyAuth"],
            json=_json,
            cast_to=models.AddressVerifyResponse,
            request_options=request_options or default_request_options(),
        )

    def auto_complete(
        self,
        *,
        search: str,
        latitude: typing.Union[
            typing.Optional[float], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        longitude: typing.Union[
            typing.Optional[float], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        precision: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        search_types: typing.Union[
            typing.Optional[
                typing.List[
                    typing_extensions.Literal["A", "C", "G", "N", "P", "T", "Z"]
                ]
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.AddressAutoCompleteResponse:
        """
        AutoComplete API

        The AutoComplete approximates like property searches based on incomplete address parts and combinations.
        Our AutoComplete algorithms are powered by machine learning and give you rich property lists
        without having to design tons of different Property Search queries.


        POST /v2/AutoComplete

        Args:
            latitude: float
            longitude: float
            precision: Coordinate precision digits
            search_types: Filter by search types
            search: Search term (minimum 3 characters)
            request_options: Additional options to customize the HTTP request

        Returns:
            AutoComplete suggestions retrieved successfully

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.address.auto_complete(search="string")
        ```
        """
        _json = to_encodable(
            item={
                "latitude": latitude,
                "longitude": longitude,
                "precision": precision,
                "search_types": search_types,
                "search": search,
            },
            dump_with=params._SerializerAutoCompleteParameters,
        )
        return self._base_client.request(
            method="POST",
            path="/v2/AutoComplete",
            auth_names=["ApiKeyAuth"],
            json=_json,
            cast_to=models.AddressAutoCompleteResponse,
            request_options=request_options or default_request_options(),
        )


class AsyncAddressClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def verify(
        self,
        *,
        addresses: typing.Union[
            typing.Optional[typing.List[params.AddressToVerify]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        strict: typing.Union[
            typing.Optional[bool], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.AddressVerifyResponse:
        """
        Address Verification API

        Verify 1 - 100 addresses at a time for accuracy and standardization.


        POST /v2/AddressVerification

        Args:
            addresses: typing.List[AddressToVerify]
            strict: Enable strict verification mode
            request_options: Additional options to customize the HTTP request

        Returns:
            Address verification results

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.address.verify()
        ```
        """
        _json = to_encodable(
            item={"addresses": addresses, "strict": strict},
            dump_with=params._SerializerAddressVerificationParameters,
        )
        return await self._base_client.request(
            method="POST",
            path="/v2/AddressVerification",
            auth_names=["ApiKeyAuth"],
            json=_json,
            cast_to=models.AddressVerifyResponse,
            request_options=request_options or default_request_options(),
        )

    async def auto_complete(
        self,
        *,
        search: str,
        latitude: typing.Union[
            typing.Optional[float], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        longitude: typing.Union[
            typing.Optional[float], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        precision: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        search_types: typing.Union[
            typing.Optional[
                typing.List[
                    typing_extensions.Literal["A", "C", "G", "N", "P", "T", "Z"]
                ]
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.AddressAutoCompleteResponse:
        """
        AutoComplete API

        The AutoComplete approximates like property searches based on incomplete address parts and combinations.
        Our AutoComplete algorithms are powered by machine learning and give you rich property lists
        without having to design tons of different Property Search queries.


        POST /v2/AutoComplete

        Args:
            latitude: float
            longitude: float
            precision: Coordinate precision digits
            search_types: Filter by search types
            search: Search term (minimum 3 characters)
            request_options: Additional options to customize the HTTP request

        Returns:
            AutoComplete suggestions retrieved successfully

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.address.auto_complete(search="string")
        ```
        """
        _json = to_encodable(
            item={
                "latitude": latitude,
                "longitude": longitude,
                "precision": precision,
                "search_types": search_types,
                "search": search,
            },
            dump_with=params._SerializerAutoCompleteParameters,
        )
        return await self._base_client.request(
            method="POST",
            path="/v2/AutoComplete",
            auth_names=["ApiKeyAuth"],
            json=_json,
            cast_to=models.AddressAutoCompleteResponse,
            request_options=request_options or default_request_options(),
        )
