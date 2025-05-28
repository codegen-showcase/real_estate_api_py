import pydantic
import typing


class FloodZoneInformation(pydantic.BaseModel):
    """
    Flood zone and environmental hazard information
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    flood_zone: typing.Optional[bool] = pydantic.Field(alias="floodZone", default=None)
    """
    Property is in a designated flood zone
    """
    flood_zone_description: typing.Optional[str] = pydantic.Field(
        alias="floodZoneDescription", default=None
    )
    """
    Description of flood zone risk level
    """
    flood_zone_type: typing.Optional[str] = pydantic.Field(
        alias="floodZoneType", default=None
    )
    """
    FEMA flood zone designation
    """
