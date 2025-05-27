import pydantic
import typing
import typing_extensions


class PropertyGenerateCsvBodyPolygonItem(typing_extensions.TypedDict):
    """
    PropertyGenerateCsvBodyPolygonItem
    """

    lat: typing_extensions.NotRequired[float]

    lon: typing_extensions.NotRequired[float]


class _SerializerPropertyGenerateCsvBodyPolygonItem(pydantic.BaseModel):
    """
    Serializer for PropertyGenerateCsvBodyPolygonItem handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    lat: typing.Optional[float] = pydantic.Field(alias="lat", default=None)
    lon: typing.Optional[float] = pydantic.Field(alias="lon", default=None)
