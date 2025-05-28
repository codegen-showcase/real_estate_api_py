import pydantic
import typing


class PropertyPinsResponseDataItem(pydantic.BaseModel):
    """
    Property data optimized for mapping display
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    address: typing.Optional[str] = pydantic.Field(alias="address", default=None)
    """
    Display address
    """
    bathrooms: typing.Optional[int] = pydantic.Field(alias="bathrooms", default=None)
    """
    Number of bathrooms
    """
    bedrooms: typing.Optional[int] = pydantic.Field(alias="bedrooms", default=None)
    """
    Number of bedrooms
    """
    estimated_value: typing.Optional[int] = pydantic.Field(
        alias="estimatedValue", default=None
    )
    """
    Estimated property value
    """
    id: typing.Optional[str] = pydantic.Field(alias="id", default=None)
    """
    Unique property identifier
    """
    last_sale_date: typing.Optional[str] = pydantic.Field(
        alias="lastSaleDate", default=None
    )
    """
    Date of last sale
    """
    last_sale_price: typing.Optional[int] = pydantic.Field(
        alias="lastSalePrice", default=None
    )
    """
    Last sale price
    """
    latitude: typing.Optional[float] = pydantic.Field(alias="latitude", default=None)
    """
    Property latitude
    """
    longitude: typing.Optional[float] = pydantic.Field(alias="longitude", default=None)
    """
    Property longitude
    """
    mls_listing_price: typing.Optional[int] = pydantic.Field(
        alias="mlsListingPrice", default=None
    )
    """
    Current MLS listing price
    """
    mls_status: typing.Optional[str] = pydantic.Field(alias="mlsStatus", default=None)
    """
    Current MLS status
    """
    property_type: typing.Optional[str] = pydantic.Field(
        alias="propertyType", default=None
    )
    """
    Property type
    """
    square_feet: typing.Optional[int] = pydantic.Field(alias="squareFeet", default=None)
    """
    Living area square footage
    """
    year_built: typing.Optional[int] = pydantic.Field(alias="yearBuilt", default=None)
    """
    Year property was built
    """
