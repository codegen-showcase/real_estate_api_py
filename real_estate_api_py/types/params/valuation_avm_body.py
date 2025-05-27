import pydantic
import typing
import typing_extensions


class ValuationAvmBody(typing_extensions.TypedDict):
    """
    ValuationAvmBody
    """

    address: typing_extensions.NotRequired[str]

    id: typing_extensions.NotRequired[str]

    strict: typing_extensions.NotRequired[bool]


class _SerializerValuationAvmBody(pydantic.BaseModel):
    """
    Serializer for ValuationAvmBody handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    address: typing.Optional[str] = pydantic.Field(alias="address", default=None)
    id: typing.Optional[str] = pydantic.Field(alias="id", default=None)
    strict: typing.Optional[bool] = pydantic.Field(alias="strict", default=None)
