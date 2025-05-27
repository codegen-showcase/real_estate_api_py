import pydantic
import typing
import typing_extensions


class PropertySearchBodyPolygonItem(typing_extensions.TypedDict):
    """
    PropertySearchBodyPolygonItem
    """

    lat: typing_extensions.NotRequired[float]

    lon: typing_extensions.NotRequired[float]


class _SerializerPropertySearchBodyPolygonItem(pydantic.BaseModel):
    """
    Serializer for PropertySearchBodyPolygonItem handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    lat: typing.Optional[float] = pydantic.Field(alias="lat", default=None)
    lon: typing.Optional[float] = pydantic.Field(alias="lon", default=None)
