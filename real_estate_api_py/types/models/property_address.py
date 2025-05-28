import pydantic
import typing


class PropertyAddress(pydantic.BaseModel):
    """
    Standardized property address information
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    address: str = pydantic.Field(
        alias="address",
    )
    """
    Complete formatted address
    """
    carrier_route: typing.Optional[str] = pydantic.Field(
        alias="carrierRoute", default=None
    )
    """
    USPS carrier route
    """
    census_tract: typing.Optional[str] = pydantic.Field(
        alias="censusTract", default=None
    )
    """
    Census tract identifier
    """
    city: str = pydantic.Field(
        alias="city",
    )
    """
    City name
    """
    congressional_district: typing.Optional[str] = pydantic.Field(
        alias="congressionalDistrict", default=None
    )
    """
    Congressional district number
    """
    county: typing.Optional[str] = pydantic.Field(alias="county", default=None)
    """
    County name
    """
    fips: typing.Optional[str] = pydantic.Field(alias="fips", default=None)
    """
    Federal Information Processing Standards (FIPS) county code
    """
    house: typing.Optional[str] = pydantic.Field(alias="house", default=None)
    """
    House number
    """
    label: typing.Optional[str] = pydantic.Field(alias="label", default=None)
    """
    Formatted address label for display
    """
    post_direction: typing.Optional[str] = pydantic.Field(
        alias="postDirection", default=None
    )
    """
    Street suffix direction
    """
    pre_direction: typing.Optional[str] = pydantic.Field(
        alias="preDirection", default=None
    )
    """
    Street prefix direction (N, S, E, W, etc.)
    """
    state: str = pydantic.Field(
        alias="state",
    )
    """
    Two-character state code
    """
    street: typing.Optional[str] = pydantic.Field(alias="street", default=None)
    """
    Street name without house number
    """
    street_type: typing.Optional[str] = pydantic.Field(alias="streetType", default=None)
    """
    Street type (St, Ave, Blvd, etc.)
    """
    unit: typing.Optional[str] = pydantic.Field(alias="unit", default=None)
    """
    Unit, suite, or apartment number
    """
    zip: str = pydantic.Field(
        alias="zip",
    )
    """
    Five-digit ZIP code
    """
    zip4: typing.Optional[str] = pydantic.Field(alias="zip4", default=None)
    """
    Four-digit ZIP+4 extension
    """
