import pydantic
import typing_extensions


class GeoCoordinate(typing_extensions.TypedDict):
    """
    GeoCoordinate
    """

    lat: typing_extensions.Required[float]
    """
    Latitude coordinate
    """

    lon: typing_extensions.Required[float]
    """
    Longitude coordinate
    """


class _SerializerGeoCoordinate(pydantic.BaseModel):
    """
    Serializer for GeoCoordinate handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    lat: float = pydantic.Field(
        alias="lat",
    )
    lon: float = pydantic.Field(
        alias="lon",
    )
