import pydantic
import typing
import typing_extensions


class PropertyDetailParameters(typing_extensions.TypedDict):
    """
    PropertyDetailParameters
    """

    address: typing_extensions.NotRequired[str]
    """
    Fully formatted address
    """

    apn: typing_extensions.NotRequired[str]
    """
    Assessor's Parcel Number
    """

    city: typing_extensions.NotRequired[str]
    """
    City name
    """

    comps: typing_extensions.NotRequired[bool]
    """
    Include comparable properties
    """

    county: typing_extensions.NotRequired[str]
    """
    County name
    """

    exact_match: typing_extensions.NotRequired[bool]
    """
    Require exact address match
    """

    fips: typing_extensions.NotRequired[str]
    """
    FIPS county code
    """

    house: typing_extensions.NotRequired[str]
    """
    House number
    """

    id: typing_extensions.NotRequired[str]
    """
    Property ID from search results
    """

    state: typing_extensions.NotRequired[str]
    """
    Two-letter state code
    """

    street: typing_extensions.NotRequired[str]
    """
    Street name
    """

    unit: typing_extensions.NotRequired[str]
    """
    Unit number
    """

    zip: typing_extensions.NotRequired[str]
    """
    5-digit ZIP code
    """


class _SerializerPropertyDetailParameters(pydantic.BaseModel):
    """
    Serializer for PropertyDetailParameters handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    address: typing.Optional[str] = pydantic.Field(alias="address", default=None)
    apn: typing.Optional[str] = pydantic.Field(alias="apn", default=None)
    city: typing.Optional[str] = pydantic.Field(alias="city", default=None)
    comps: typing.Optional[bool] = pydantic.Field(alias="comps", default=None)
    county: typing.Optional[str] = pydantic.Field(alias="county", default=None)
    exact_match: typing.Optional[bool] = pydantic.Field(
        alias="exact_match", default=None
    )
    fips: typing.Optional[str] = pydantic.Field(alias="fips", default=None)
    house: typing.Optional[str] = pydantic.Field(alias="house", default=None)
    id: typing.Optional[str] = pydantic.Field(alias="id", default=None)
    state: typing.Optional[str] = pydantic.Field(alias="state", default=None)
    street: typing.Optional[str] = pydantic.Field(alias="street", default=None)
    unit: typing.Optional[str] = pydantic.Field(alias="unit", default=None)
    zip: typing.Optional[str] = pydantic.Field(alias="zip", default=None)
