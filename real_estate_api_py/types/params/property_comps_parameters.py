import pydantic
import typing
import typing_extensions


class PropertyCompsParameters(typing_extensions.TypedDict):
    """
    PropertyCompsParameters
    """

    address: typing_extensions.NotRequired[str]
    """
    Fully formatted address
    """

    id: typing_extensions.NotRequired[str]
    """
    Property ID
    """


class _SerializerPropertyCompsParameters(pydantic.BaseModel):
    """
    Serializer for PropertyCompsParameters handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    address: typing.Optional[str] = pydantic.Field(alias="address", default=None)
    id: typing.Optional[str] = pydantic.Field(alias="id", default=None)
