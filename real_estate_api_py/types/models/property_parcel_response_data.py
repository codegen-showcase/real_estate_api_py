import pydantic
import typing
import typing_extensions

from .property_parcel_response_data_features_item import (
    PropertyParcelResponseDataFeaturesItem,
)


class PropertyParcelResponseData(pydantic.BaseModel):
    """
    GeoJSON FeatureCollection containing property boundaries
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    features: typing.Optional[typing.List[PropertyParcelResponseDataFeaturesItem]] = (
        pydantic.Field(alias="features", default=None)
    )
    type_: typing.Optional[typing_extensions.Literal["FeatureCollection"]] = (
        pydantic.Field(alias="type", default=None)
    )
