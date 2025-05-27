import pydantic
import typing
import typing_extensions

from .property_generate_csv_body_multi_polygon_item_boundaries_item import (
    PropertyGenerateCsvBodyMultiPolygonItemBoundariesItem,
    _SerializerPropertyGenerateCsvBodyMultiPolygonItemBoundariesItem,
)


class PropertyGenerateCsvBodyMultiPolygonItem(typing_extensions.TypedDict):
    """
    PropertyGenerateCsvBodyMultiPolygonItem
    """

    boundaries: typing_extensions.NotRequired[
        typing.List[PropertyGenerateCsvBodyMultiPolygonItemBoundariesItem]
    ]


class _SerializerPropertyGenerateCsvBodyMultiPolygonItem(pydantic.BaseModel):
    """
    Serializer for PropertyGenerateCsvBodyMultiPolygonItem handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    boundaries: typing.Optional[
        typing.List[_SerializerPropertyGenerateCsvBodyMultiPolygonItemBoundariesItem]
    ] = pydantic.Field(alias="boundaries", default=None)
