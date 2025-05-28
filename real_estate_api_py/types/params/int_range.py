import pydantic
import typing
import typing_extensions


class IntRange(typing_extensions.TypedDict):
    """
    IntRange
    """

    max: typing_extensions.NotRequired[int]

    min: typing_extensions.NotRequired[int]


class _SerializerIntRange(pydantic.BaseModel):
    """
    Serializer for IntRange handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    max: typing.Optional[int] = pydantic.Field(alias="max", default=None)
    min: typing.Optional[int] = pydantic.Field(alias="min", default=None)
