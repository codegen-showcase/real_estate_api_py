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


class GptClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def chat(
        self,
        *,
        x_api_key: str,
        x_openai_key: str,
        data: typing.Union[
            typing.Optional[params.GptChatBody], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> str:
        """
        PropGPT API

        Check out the functionality of this endpoint at https://www.propgpt.com

        POST /v2/PropGPT

        Args:
            data: GptChatBody
            x-api-key: str
            x-openai-key: Sign up with OpenAI (at https://openai.com/blog/openai-api) and get your free API Key to attach to all your requests to this endpoint for token spend tracking.
            request_options: Additional options to customize the HTTP request

        Returns:
            200

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.gpt.chat(x_api_key="string", x_openai_key="string")
        ```
        """
        _header: typing.Dict[str, str] = {}
        _header["x-api-key"] = str(x_api_key)
        _header["x-openai-key"] = str(x_openai_key)
        _json = (
            to_encodable(item=data, dump_with=params._SerializerGptChatBody)
            if data
            else None
        )
        return self._base_client.request(
            method="POST",
            path="/v2/PropGPT",
            auth_names=["sec0"],
            headers=_header,
            json=_json,
            cast_to=str,
            request_options=request_options or default_request_options(),
        )


class AsyncGptClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def chat(
        self,
        *,
        x_api_key: str,
        x_openai_key: str,
        data: typing.Union[
            typing.Optional[params.GptChatBody], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> str:
        """
        PropGPT API

        Check out the functionality of this endpoint at https://www.propgpt.com

        POST /v2/PropGPT

        Args:
            data: GptChatBody
            x-api-key: str
            x-openai-key: Sign up with OpenAI (at https://openai.com/blog/openai-api) and get your free API Key to attach to all your requests to this endpoint for token spend tracking.
            request_options: Additional options to customize the HTTP request

        Returns:
            200

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.gpt.chat(x_api_key="string", x_openai_key="string")
        ```
        """
        _header: typing.Dict[str, str] = {}
        _header["x-api-key"] = str(x_api_key)
        _header["x-openai-key"] = str(x_openai_key)
        _json = (
            to_encodable(item=data, dump_with=params._SerializerGptChatBody)
            if data
            else None
        )
        return await self._base_client.request(
            method="POST",
            path="/v2/PropGPT",
            auth_names=["sec0"],
            headers=_header,
            json=_json,
            cast_to=str,
            request_options=request_options or default_request_options(),
        )
