import pydantic
import typing
import typing_extensions


class PropertyDetailPropertyInfo(pydantic.BaseModel):
    """
    PropertyDetailPropertyInfo
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    bathrooms: typing.Optional[int] = pydantic.Field(alias="bathrooms", default=None)
    """
    Number of full bathrooms
    """
    bedrooms: typing.Optional[int] = pydantic.Field(alias="bedrooms", default=None)
    """
    Number of bedrooms
    """
    building_square_feet: typing.Optional[int] = pydantic.Field(
        alias="buildingSquareFeet", default=None
    )
    """
    Total building square footage including non-living areas
    """
    land_use: typing.Optional[str] = pydantic.Field(alias="landUse", default=None)
    """
    Land use classification
    """
    living_square_feet: typing.Optional[int] = pydantic.Field(
        alias="livingSquareFeet", default=None
    )
    """
    Heated/cooled living area square footage
    """
    lot_acres: typing.Optional[float] = pydantic.Field(alias="lotAcres", default=None)
    """
    Lot size in acres
    """
    lot_square_feet: typing.Optional[int] = pydantic.Field(
        alias="lotSquareFeet", default=None
    )
    """
    Lot size in square feet
    """
    parking_spaces: typing.Optional[int] = pydantic.Field(
        alias="parkingSpaces", default=None
    )
    """
    Number of parking spaces
    """
    partial_bathrooms: typing.Optional[int] = pydantic.Field(
        alias="partialBathrooms", default=None
    )
    """
    Number of partial/half bathrooms
    """
    property_type: typing.Optional[
        typing_extensions.Literal["CONDO", "LAND", "MFR", "MOBILE", "OTHER", "SFR"]
    ] = pydantic.Field(alias="propertyType", default=None)
    """
    Primary property type classification
    """
    property_use: typing.Optional[str] = pydantic.Field(
        alias="propertyUse", default=None
    )
    """
    Detailed property use description
    """
    property_use_code: typing.Optional[int] = pydantic.Field(
        alias="propertyUseCode", default=None
    )
    """
    Numeric code for property use type
    """
    rooms_count: typing.Optional[int] = pydantic.Field(alias="roomsCount", default=None)
    """
    Total number of rooms
    """
    square_feet: typing.Optional[int] = pydantic.Field(alias="squareFeet", default=None)
    """
    Living area square footage
    """
    stories: typing.Optional[int] = pydantic.Field(alias="stories", default=None)
    """
    Number of stories/floors
    """
    units_count: typing.Optional[int] = pydantic.Field(alias="unitsCount", default=None)
    """
    Number of units (for multi-family properties)
    """
    year_built: typing.Optional[int] = pydantic.Field(alias="yearBuilt", default=None)
    """
    Year the property was built
    """
    air_conditioning_available: typing.Optional[bool] = pydantic.Field(
        alias="airConditioningAvailable", default=None
    )
    """
    Property has air conditioning
    """
    attic: typing.Optional[bool] = pydantic.Field(alias="attic", default=None)
    """
    Property has an attic
    """
    basement: typing.Optional[bool] = pydantic.Field(alias="basement", default=None)
    """
    Property has a basement
    """
    basement_square_feet: typing.Optional[int] = pydantic.Field(
        alias="basementSquareFeet", default=None
    )
    """
    Total basement area in square feet
    """
    basement_square_feet_finished: typing.Optional[int] = pydantic.Field(
        alias="basementSquareFeetFinished", default=None
    )
    """
    Finished basement area in square feet
    """
    basement_square_feet_unfinished: typing.Optional[int] = pydantic.Field(
        alias="basementSquareFeetUnfinished", default=None
    )
    """
    Unfinished basement area in square feet
    """
    basement_type: typing.Optional[str] = pydantic.Field(
        alias="basementType", default=None
    )
    """
    Type of basement
    """
    carport: typing.Optional[bool] = pydantic.Field(alias="carport", default=None)
    """
    Property has a carport
    """
    deck: typing.Optional[bool] = pydantic.Field(alias="deck", default=None)
    """
    Property has a deck
    """
    deck_area: typing.Optional[int] = pydantic.Field(alias="deckArea", default=None)
    """
    Deck area in square feet
    """
    fireplace: typing.Optional[bool] = pydantic.Field(alias="fireplace", default=None)
    """
    Property has a fireplace
    """
    fireplaces: typing.Optional[int] = pydantic.Field(alias="fireplaces", default=None)
    """
    Number of fireplaces
    """
    garage: typing.Optional[bool] = pydantic.Field(alias="garage", default=None)
    """
    Property has a garage
    """
    garage_square_feet: typing.Optional[int] = pydantic.Field(
        alias="garageSquareFeet", default=None
    )
    """
    Garage area in square feet
    """
    garage_type: typing.Optional[str] = pydantic.Field(alias="garageType", default=None)
    """
    Type of garage
    """
    heating_fuel_type: typing.Optional[str] = pydantic.Field(
        alias="heatingFuelType", default=None
    )
    """
    Fuel type for heating system
    """
    heating_type: typing.Optional[str] = pydantic.Field(
        alias="heatingType", default=None
    )
    """
    Type of heating system
    """
    patio: typing.Optional[bool] = pydantic.Field(alias="patio", default=None)
    """
    Property has a patio
    """
    pool: typing.Optional[bool] = pydantic.Field(alias="pool", default=None)
    """
    Property has a swimming pool
    """
    pool_area: typing.Optional[int] = pydantic.Field(alias="poolArea", default=None)
    """
    Pool area in square feet
    """
    rv_parking: typing.Optional[bool] = pydantic.Field(alias="rvParking", default=None)
    """
    Property has RV parking
    """
    latitude: float = pydantic.Field(
        alias="latitude",
    )
    """
    Property latitude coordinate (WGS84)
    """
    longitude: float = pydantic.Field(
        alias="longitude",
    )
    """
    Property longitude coordinate (WGS84)
    """
