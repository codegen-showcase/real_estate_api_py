import pydantic
import typing
import typing_extensions

from .property_search_body_multi_polygon_item_boundaries_item import (
    PropertySearchBodyMultiPolygonItemBoundariesItem,
    _SerializerPropertySearchBodyMultiPolygonItemBoundariesItem,
)


class PropertySearchBodyMultiPolygonItem(typing_extensions.TypedDict):
    """
    PropertySearchBodyMultiPolygonItem
    """

    boundaries: typing_extensions.NotRequired[
        typing.List[PropertySearchBodyMultiPolygonItemBoundariesItem]
    ]


class _SerializerPropertySearchBodyMultiPolygonItem(pydantic.BaseModel):
    """
    Serializer for PropertySearchBodyMultiPolygonItem handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    boundaries: typing.Optional[
        typing.List[_SerializerPropertySearchBodyMultiPolygonItemBoundariesItem]
    ] = pydantic.Field(alias="boundaries", default=None)
