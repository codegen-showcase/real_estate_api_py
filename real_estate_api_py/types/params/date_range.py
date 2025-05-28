import pydantic
import typing
import typing_extensions


class DateRange(typing_extensions.TypedDict):
    """
    DateRange
    """

    max: typing_extensions.NotRequired[str]

    min: typing_extensions.NotRequired[str]


class _SerializerDateRange(pydantic.BaseModel):
    """
    Serializer for DateRange handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    max: typing.Optional[str] = pydantic.Field(alias="max", default=None)
    min: typing.Optional[str] = pydantic.Field(alias="min", default=None)
