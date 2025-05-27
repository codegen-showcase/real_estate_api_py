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


class PropertyClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def generate_csv(
        self,
        *,
        data: typing.Union[
            typing.Optional[params.PropertyGenerateCsvBody], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        CSV Generator API



        POST /v2/CSVBuilder

        Args:
            data: PropertyGenerateCsvBody
            request_options: Additional options to customize the HTTP request

        Returns:
            200

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.property.generate_csv()
        ```
        """
        _json = (
            to_encodable(item=data, dump_with=params._SerializerPropertyGenerateCsvBody)
            if data
            else None
        )
        return self._base_client.request(
            method="POST",
            path="/v2/CSVBuilder",
            auth_names=["sec0"],
            json=_json,
            cast_to=typing.Dict[str, typing.Any],
            request_options=request_options or default_request_options(),
        )

    def comps_standard(
        self,
        *,
        data: typing.Union[
            typing.Optional[params.PropertyCompsStandardBody], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Any:
        """
        v2/PropertyComps API



        POST /v2/PropertyComps

        Args:
            data: PropertyCompsStandardBody
            request_options: Additional options to customize the HTTP request

        Returns:
            200

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.property.comps_standard()
        ```
        """
        _json = (
            to_encodable(
                item=data, dump_with=params._SerializerPropertyCompsStandardBody
            )
            if data
            else None
        )
        return self._base_client.request(
            method="POST",
            path="/v2/PropertyComps",
            auth_names=["sec0"],
            json=_json,
            cast_to=type(typing.Any),
            request_options=request_options or default_request_options(),
        )

    def details(
        self,
        *,
        data: typing.Union[
            typing.Optional[params.PropertyDetailsBody], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Any:
        """
        Property Detail API

        Comps, Mortgages, Mailing Addresses, Property Sales History & More!

        POST /v2/PropertyDetail

        Args:
            data: PropertyDetailsBody
            request_options: Additional options to customize the HTTP request

        Returns:
            200

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.property.details()
        ```
        """
        _json = (
            to_encodable(item=data, dump_with=params._SerializerPropertyDetailsBody)
            if data
            else None
        )
        return self._base_client.request(
            method="POST",
            path="/v2/PropertyDetail",
            auth_names=["sec0"],
            json=_json,
            cast_to=type(typing.Any),
            request_options=request_options or default_request_options(),
        )

    def details_bulk(
        self,
        *,
        data: typing.Union[
            typing.Optional[params.PropertyDetailsBulkBody], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Any:
        """
        Property Detail Bulk API

        For retrieving of up to 1000 properties at once.  Can be used standalone, but it's designed to work together with the Property Search API.  Use this API for quickly exporting lists, or bulk search requests for analytics.  Pass in addresses, or a list of ID's returned from the Property Search API.

        POST /v2/PropertyDetailBulk

        Args:
            data: PropertyDetailsBulkBody
            request_options: Additional options to customize the HTTP request

        Returns:
            200

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.property.details_bulk()
        ```
        """
        _json = (
            to_encodable(item=data, dump_with=params._SerializerPropertyDetailsBulkBody)
            if data
            else None
        )
        return self._base_client.request(
            method="POST",
            path="/v2/PropertyDetailBulk",
            auth_names=["sec0"],
            json=_json,
            cast_to=type(typing.Any),
            request_options=request_options or default_request_options(),
        )

    def pins(
        self,
        *,
        data: typing.Union[
            typing.Optional[params.PropertyPinsBody], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        [BETA] Mapping ("Pins") API

        Have your PropTech Maps Come to Life with Unlimited "Pins" on a Map API. Only available on Growth+ Plans

        POST /v2/PropertyMapping

        Args:
            data: PropertyPinsBody
            request_options: Additional options to customize the HTTP request

        Returns:
            200

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.property.pins()
        ```
        """
        _json = (
            to_encodable(item=data, dump_with=params._SerializerPropertyPinsBody)
            if data
            else None
        )
        return self._base_client.request(
            method="POST",
            path="/v2/PropertyMapping",
            auth_names=["sec0"],
            json=_json,
            cast_to=typing.Dict[str, typing.Any],
            request_options=request_options or default_request_options(),
        )

    def search(
        self,
        *,
        x_api_key: str,
        data: typing.Union[
            typing.Optional[params.PropertySearchBody], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Union[
        models.PropertySearchResponseObj0,
        models.PropertySearchResponseObj1,
        models.PropertySearchResponseObj2,
        models.PropertySearchResponseObj3,
    ]:
        """
        Property Search API

        Searchable API for list building, search counts, and advanced filtering on properties.  You can also use this API to implement your own comparables API, or property analytics API.  Questions?  Contact our team to ask us for best practices with using this API.This API implements easy paging so your apps can easily manage filtered results in a results pane with paging.  When your user clicks on a result, just use the id from this API to get the full property results using the Property Detail API.  Questions on best practices for implementing paged property results in your app?  Just contact our team.

        POST /v2/PropertySearch

        Args:
            data: PropertySearchBody
            x-api-key: User's API key
            request_options: Additional options to customize the HTTP request

        Returns:
            200

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.property.search(x_api_key="string")
        ```
        """
        _header: typing.Dict[str, str] = {}
        _header["x-api-key"] = str(x_api_key)
        _json = (
            to_encodable(item=data, dump_with=params._SerializerPropertySearchBody)
            if data
            else None
        )
        return self._base_client.request(
            method="POST",
            path="/v2/PropertySearch",
            auth_names=["sec0"],
            headers=_header,
            json=_json,
            cast_to=typing.Union[
                models.PropertySearchResponseObj0,
                models.PropertySearchResponseObj1,
                models.PropertySearchResponseObj2,
                models.PropertySearchResponseObj3,
            ],
            request_options=request_options or default_request_options(),
        )

    def comps_custom(
        self,
        *,
        data: typing.Union[
            typing.Optional[params.PropertyCompsCustomBody], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        /v3/PropertyComps API

        Customize your comps model

        POST /v3/PropertyComps

        Args:
            data: PropertyCompsCustomBody
            request_options: Additional options to customize the HTTP request

        Returns:
            200

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.property.comps_custom()
        ```
        """
        _json = (
            to_encodable(item=data, dump_with=params._SerializerPropertyCompsCustomBody)
            if data
            else None
        )
        return self._base_client.request(
            method="POST",
            path="/v3/PropertyComps",
            auth_names=["sec0"],
            json=_json,
            cast_to=typing.Dict[str, typing.Any],
            request_options=request_options or default_request_options(),
        )


class AsyncPropertyClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def generate_csv(
        self,
        *,
        data: typing.Union[
            typing.Optional[params.PropertyGenerateCsvBody], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        CSV Generator API



        POST /v2/CSVBuilder

        Args:
            data: PropertyGenerateCsvBody
            request_options: Additional options to customize the HTTP request

        Returns:
            200

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.property.generate_csv()
        ```
        """
        _json = (
            to_encodable(item=data, dump_with=params._SerializerPropertyGenerateCsvBody)
            if data
            else None
        )
        return await self._base_client.request(
            method="POST",
            path="/v2/CSVBuilder",
            auth_names=["sec0"],
            json=_json,
            cast_to=typing.Dict[str, typing.Any],
            request_options=request_options or default_request_options(),
        )

    async def comps_standard(
        self,
        *,
        data: typing.Union[
            typing.Optional[params.PropertyCompsStandardBody], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Any:
        """
        v2/PropertyComps API



        POST /v2/PropertyComps

        Args:
            data: PropertyCompsStandardBody
            request_options: Additional options to customize the HTTP request

        Returns:
            200

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.property.comps_standard()
        ```
        """
        _json = (
            to_encodable(
                item=data, dump_with=params._SerializerPropertyCompsStandardBody
            )
            if data
            else None
        )
        return await self._base_client.request(
            method="POST",
            path="/v2/PropertyComps",
            auth_names=["sec0"],
            json=_json,
            cast_to=type(typing.Any),
            request_options=request_options or default_request_options(),
        )

    async def details(
        self,
        *,
        data: typing.Union[
            typing.Optional[params.PropertyDetailsBody], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Any:
        """
        Property Detail API

        Comps, Mortgages, Mailing Addresses, Property Sales History & More!

        POST /v2/PropertyDetail

        Args:
            data: PropertyDetailsBody
            request_options: Additional options to customize the HTTP request

        Returns:
            200

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.property.details()
        ```
        """
        _json = (
            to_encodable(item=data, dump_with=params._SerializerPropertyDetailsBody)
            if data
            else None
        )
        return await self._base_client.request(
            method="POST",
            path="/v2/PropertyDetail",
            auth_names=["sec0"],
            json=_json,
            cast_to=type(typing.Any),
            request_options=request_options or default_request_options(),
        )

    async def details_bulk(
        self,
        *,
        data: typing.Union[
            typing.Optional[params.PropertyDetailsBulkBody], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Any:
        """
        Property Detail Bulk API

        For retrieving of up to 1000 properties at once.  Can be used standalone, but it's designed to work together with the Property Search API.  Use this API for quickly exporting lists, or bulk search requests for analytics.  Pass in addresses, or a list of ID's returned from the Property Search API.

        POST /v2/PropertyDetailBulk

        Args:
            data: PropertyDetailsBulkBody
            request_options: Additional options to customize the HTTP request

        Returns:
            200

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.property.details_bulk()
        ```
        """
        _json = (
            to_encodable(item=data, dump_with=params._SerializerPropertyDetailsBulkBody)
            if data
            else None
        )
        return await self._base_client.request(
            method="POST",
            path="/v2/PropertyDetailBulk",
            auth_names=["sec0"],
            json=_json,
            cast_to=type(typing.Any),
            request_options=request_options or default_request_options(),
        )

    async def pins(
        self,
        *,
        data: typing.Union[
            typing.Optional[params.PropertyPinsBody], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        [BETA] Mapping ("Pins") API

        Have your PropTech Maps Come to Life with Unlimited "Pins" on a Map API. Only available on Growth+ Plans

        POST /v2/PropertyMapping

        Args:
            data: PropertyPinsBody
            request_options: Additional options to customize the HTTP request

        Returns:
            200

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.property.pins()
        ```
        """
        _json = (
            to_encodable(item=data, dump_with=params._SerializerPropertyPinsBody)
            if data
            else None
        )
        return await self._base_client.request(
            method="POST",
            path="/v2/PropertyMapping",
            auth_names=["sec0"],
            json=_json,
            cast_to=typing.Dict[str, typing.Any],
            request_options=request_options or default_request_options(),
        )

    async def search(
        self,
        *,
        x_api_key: str,
        data: typing.Union[
            typing.Optional[params.PropertySearchBody], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Union[
        models.PropertySearchResponseObj0,
        models.PropertySearchResponseObj1,
        models.PropertySearchResponseObj2,
        models.PropertySearchResponseObj3,
    ]:
        """
        Property Search API

        Searchable API for list building, search counts, and advanced filtering on properties.  You can also use this API to implement your own comparables API, or property analytics API.  Questions?  Contact our team to ask us for best practices with using this API.This API implements easy paging so your apps can easily manage filtered results in a results pane with paging.  When your user clicks on a result, just use the id from this API to get the full property results using the Property Detail API.  Questions on best practices for implementing paged property results in your app?  Just contact our team.

        POST /v2/PropertySearch

        Args:
            data: PropertySearchBody
            x-api-key: User's API key
            request_options: Additional options to customize the HTTP request

        Returns:
            200

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.property.search(x_api_key="string")
        ```
        """
        _header: typing.Dict[str, str] = {}
        _header["x-api-key"] = str(x_api_key)
        _json = (
            to_encodable(item=data, dump_with=params._SerializerPropertySearchBody)
            if data
            else None
        )
        return await self._base_client.request(
            method="POST",
            path="/v2/PropertySearch",
            auth_names=["sec0"],
            headers=_header,
            json=_json,
            cast_to=typing.Union[
                models.PropertySearchResponseObj0,
                models.PropertySearchResponseObj1,
                models.PropertySearchResponseObj2,
                models.PropertySearchResponseObj3,
            ],
            request_options=request_options or default_request_options(),
        )

    async def comps_custom(
        self,
        *,
        data: typing.Union[
            typing.Optional[params.PropertyCompsCustomBody], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        /v3/PropertyComps API

        Customize your comps model

        POST /v3/PropertyComps

        Args:
            data: PropertyCompsCustomBody
            request_options: Additional options to customize the HTTP request

        Returns:
            200

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.property.comps_custom()
        ```
        """
        _json = (
            to_encodable(item=data, dump_with=params._SerializerPropertyCompsCustomBody)
            if data
            else None
        )
        return await self._base_client.request(
            method="POST",
            path="/v3/PropertyComps",
            auth_names=["sec0"],
            json=_json,
            cast_to=typing.Dict[str, typing.Any],
            request_options=request_options or default_request_options(),
        )
