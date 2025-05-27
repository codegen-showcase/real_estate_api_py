import pydantic
import typing
import typing_extensions


class PropertyGenerateCsvBodyMultiPolygonItemBoundariesItem(
    typing_extensions.TypedDict
):
    """
    PropertyGenerateCsvBodyMultiPolygonItemBoundariesItem
    """

    lat: typing_extensions.NotRequired[float]

    lon: typing_extensions.NotRequired[float]


class _SerializerPropertyGenerateCsvBodyMultiPolygonItemBoundariesItem(
    pydantic.BaseModel
):
    """
    Serializer for PropertyGenerateCsvBodyMultiPolygonItemBoundariesItem handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    lat: typing.Optional[float] = pydantic.Field(alias="lat", default=None)
    lon: typing.Optional[float] = pydantic.Field(alias="lon", default=None)
