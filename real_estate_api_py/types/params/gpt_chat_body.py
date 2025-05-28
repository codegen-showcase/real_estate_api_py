import pydantic
import typing
import typing_extensions


class GptChatBody(typing_extensions.TypedDict):
    """
    GptChatBody
    """

    model: typing_extensions.NotRequired[
        typing_extensions.Literal[
            "gpt-3.5-turbo", "gpt-4", "gpt-4-turbo", "gpt-4o", "gpt-4o-mini"
        ]
    ]
    """
    OpenAI model to use for query processing
    """

    query: typing_extensions.Required[str]
    """
    Natural language string that references data points for property search
    """

    size: typing_extensions.NotRequired[int]
    """
    Maximum number of results to return
    """


class _SerializerGptChatBody(pydantic.BaseModel):
    """
    Serializer for GptChatBody handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    model: typing.Optional[
        typing_extensions.Literal[
            "gpt-3.5-turbo", "gpt-4", "gpt-4-turbo", "gpt-4o", "gpt-4o-mini"
        ]
    ] = pydantic.Field(alias="model", default=None)
    query: str = pydantic.Field(
        alias="query",
    )
    size: typing.Optional[int] = pydantic.Field(alias="size", default=None)
