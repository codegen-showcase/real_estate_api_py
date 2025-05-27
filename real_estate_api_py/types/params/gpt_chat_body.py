import pydantic
import typing
import typing_extensions


class GptChatBody(typing_extensions.TypedDict):
    """
    GptChatBody
    """

    model: typing_extensions.NotRequired[str]
    """
    Options: gpt-4, gpt-4o, gpt-4o-mini, gpt-4-turbo, gpt-3.5-turbo
    """

    query: typing_extensions.Required[str]
    """
    A natural language string that references data points in the Property Search API in order to retrieve a list of properties.
    """

    size: typing_extensions.NotRequired[int]
    """
    Maximum of 250
    """


class _SerializerGptChatBody(pydantic.BaseModel):
    """
    Serializer for GptChatBody handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    model: typing.Optional[str] = pydantic.Field(alias="model", default=None)
    query: str = pydantic.Field(
        alias="query",
    )
    size: typing.Optional[int] = pydantic.Field(alias="size", default=None)
