import pydantic
import typing
import typing_extensions


class PropertyCompsStandardBody(typing_extensions.TypedDict):
    """
    PropertyCompsStandardBody
    """

    address: typing_extensions.NotRequired[str]
    """
    A fully formatted address with the following form: 123 Main St, City State Zip
    """

    id: typing_extensions.NotRequired[int]
    """
    Property ID of an object returned by our Property Search API
    """


class _SerializerPropertyCompsStandardBody(pydantic.BaseModel):
    """
    Serializer for PropertyCompsStandardBody handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    address: typing.Optional[str] = pydantic.Field(alias="address", default=None)
    id: typing.Optional[int] = pydantic.Field(alias="id", default=None)
