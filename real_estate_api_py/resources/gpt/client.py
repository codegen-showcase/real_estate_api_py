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


class GptClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def chat(
        self,
        *,
        query: str,
        x_api_key: str,
        x_openai_key: str,
        model: typing.Union[
            typing.Optional[
                typing_extensions.Literal[
                    "gpt-3.5-turbo", "gpt-4", "gpt-4-turbo", "gpt-4o", "gpt-4o-mini"
                ]
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        size: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.GptChatResponse:
        """
        PropGPT API

        Natural language property search using AI. Convert natural language queries
        into structured property searches. Check out the functionality at https://www.propgpt.com


        POST /v2/PropGPT

        Args:
            model: OpenAI model to use for query processing
            size: Maximum number of results to return
            query: Natural language string that references data points for property search
            x-api-key: Your Real Estate API key
            x-openai-key: Your OpenAI API key for token spend tracking
            request_options: Additional options to customize the HTTP request

        Returns:
            AI-powered property search results

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.gpt.chat(
            query="Find all properties listed for sale in Herndon Virginia between 600K and 700K",
            x_api_key="string",
            x_openai_key="string",
        )
        ```
        """
        _header: typing.Dict[str, str] = {}
        _header["x-api-key"] = str(x_api_key)
        _header["x-openai-key"] = str(x_openai_key)
        _json = to_encodable(
            item={"model": model, "size": size, "query": query},
            dump_with=params._SerializerGptChatBody,
        )
        return self._base_client.request(
            method="POST",
            path="/v2/PropGPT",
            auth_names=["ApiKeyAuth"],
            headers=_header,
            json=_json,
            cast_to=models.GptChatResponse,
            request_options=request_options or default_request_options(),
        )


class AsyncGptClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def chat(
        self,
        *,
        query: str,
        x_api_key: str,
        x_openai_key: str,
        model: typing.Union[
            typing.Optional[
                typing_extensions.Literal[
                    "gpt-3.5-turbo", "gpt-4", "gpt-4-turbo", "gpt-4o", "gpt-4o-mini"
                ]
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        size: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.GptChatResponse:
        """
        PropGPT API

        Natural language property search using AI. Convert natural language queries
        into structured property searches. Check out the functionality at https://www.propgpt.com


        POST /v2/PropGPT

        Args:
            model: OpenAI model to use for query processing
            size: Maximum number of results to return
            query: Natural language string that references data points for property search
            x-api-key: Your Real Estate API key
            x-openai-key: Your OpenAI API key for token spend tracking
            request_options: Additional options to customize the HTTP request

        Returns:
            AI-powered property search results

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.gpt.chat(
            query="Find all properties listed for sale in Herndon Virginia between 600K and 700K",
            x_api_key="string",
            x_openai_key="string",
        )
        ```
        """
        _header: typing.Dict[str, str] = {}
        _header["x-api-key"] = str(x_api_key)
        _header["x-openai-key"] = str(x_openai_key)
        _json = to_encodable(
            item={"model": model, "size": size, "query": query},
            dump_with=params._SerializerGptChatBody,
        )
        return await self._base_client.request(
            method="POST",
            path="/v2/PropGPT",
            auth_names=["ApiKeyAuth"],
            headers=_header,
            json=_json,
            cast_to=models.GptChatResponse,
            request_options=request_options or default_request_options(),
        )
