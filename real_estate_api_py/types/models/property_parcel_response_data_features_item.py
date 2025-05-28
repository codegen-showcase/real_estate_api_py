import pydantic
import typing
import typing_extensions


class PropertyParcelResponseDataFeaturesItem(pydantic.BaseModel):
    """
    PropertyParcelResponseDataFeaturesItem
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    geometry: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(
        alias="geometry", default=None
    )
    """
    GeoJSON geometry object
    """
    properties: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(
        alias="properties", default=None
    )
    """
    Property metadata
    """
    type_: typing.Optional[typing_extensions.Literal["Feature"]] = pydantic.Field(
        alias="type", default=None
    )
