import pydantic
import typing
import typing_extensions

from .geo_coordinate import GeoCoordinate, _SerializerGeoCoordinate


class ReportingGenerateCsvBodyMultiPolygonItem(typing_extensions.TypedDict):
    """
    ReportingGenerateCsvBodyMultiPolygonItem
    """

    boundaries: typing_extensions.NotRequired[typing.List[GeoCoordinate]]


class _SerializerReportingGenerateCsvBodyMultiPolygonItem(pydantic.BaseModel):
    """
    Serializer for ReportingGenerateCsvBodyMultiPolygonItem handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    boundaries: typing.Optional[typing.List[_SerializerGeoCoordinate]] = pydantic.Field(
        alias="boundaries", default=None
    )
