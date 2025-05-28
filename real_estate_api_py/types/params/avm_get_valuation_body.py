import pydantic
import typing
import typing_extensions


class AvmGetValuationBody(typing_extensions.TypedDict):
    """
    AvmGetValuationBody
    """

    address: typing_extensions.NotRequired[str]
    """
    Fully formatted address
    """

    id: typing_extensions.NotRequired[str]
    """
    Property ID from search results
    """

    strict: typing_extensions.NotRequired[bool]
    """
    Enable strict address matching
    """


class _SerializerAvmGetValuationBody(pydantic.BaseModel):
    """
    Serializer for AvmGetValuationBody handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    address: typing.Optional[str] = pydantic.Field(alias="address", default=None)
    id: typing.Optional[str] = pydantic.Field(alias="id", default=None)
    strict: typing.Optional[bool] = pydantic.Field(alias="strict", default=None)
