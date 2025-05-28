import pydantic
import typing
import typing_extensions

from .geo_coordinate import GeoCoordinate, _SerializerGeoCoordinate


class PropertySearchParametersMultiPolygonItem(typing_extensions.TypedDict):
    """
    PropertySearchParametersMultiPolygonItem
    """

    boundaries: typing_extensions.NotRequired[typing.List[GeoCoordinate]]


class _SerializerPropertySearchParametersMultiPolygonItem(pydantic.BaseModel):
    """
    Serializer for PropertySearchParametersMultiPolygonItem handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    boundaries: typing.Optional[typing.List[_SerializerGeoCoordinate]] = pydantic.Field(
        alias="boundaries", default=None
    )
