import pydantic
import typing
import typing_extensions


class PropertyDetailsBody(typing_extensions.TypedDict):
    """
    PropertyDetailsBody
    """

    address: typing_extensions.NotRequired[str]
    """
    A fully formatted address with the following format: 123 Main St, Arlington VA 22205. When this field is provided and is in the valid format, no other fields are required
    """

    apn: typing_extensions.NotRequired[str]
    """
    The assessor's parcel number (APN) is a unique identifier for an address/parcel & is particularly helpful when looking up Land Parcels without House Numbers
    """

    city: typing_extensions.NotRequired[str]
    """
    The city where the property is located
    """

    comps: typing_extensions.NotRequired[bool]
    """
    Set to true if you would like to have houses nearby with conferable valuations returned as part of the response. ***Includes RealEstateAPI's special AVM for the property***
    """

    county: typing_extensions.NotRequired[str]
    """
    (*This field is not required for a fully formatted address*) The county where your search property is located.
    """

    exact_match: typing_extensions.NotRequired[bool]
    """
    only return matches that match your exact address or address parts, no fuzzy matching
    """

    fips: typing_extensions.NotRequired[str]
    """
    String of Length 5
    """

    house: typing_extensions.NotRequired[str]
    """
    House number field is to be used with the street, city, state, and zip fields (& unit if applicable)
    """

    id: typing_extensions.NotRequired[str]
    """
    The "id" property from the Property Search API result objects. If using this unique property ID for Property Detail, then no other fields are required.
    """

    state: typing_extensions.NotRequired[str]
    """
    The 2 character state code for the property's state (e.g. VA = Virginia)
    """

    street: typing_extensions.NotRequired[str]
    """
    The street name of the property (e.g. Main St)
    """

    unit: typing_extensions.NotRequired[str]
    """
    House unit number (for Apt. #'s, Suite #'s, etc.)
    """

    zip: typing_extensions.NotRequired[str]
    """
    Zipcodes need to be 5 digits
    """


class _SerializerPropertyDetailsBody(pydantic.BaseModel):
    """
    Serializer for PropertyDetailsBody handling case conversions
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
