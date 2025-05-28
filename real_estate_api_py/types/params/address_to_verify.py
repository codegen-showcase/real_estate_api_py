import pydantic
import typing
import typing_extensions


class AddressToVerify(typing_extensions.TypedDict):
    """
    AddressToVerify
    """

    address: typing_extensions.NotRequired[str]
    """
    Complete formatted address
    """

    apn: typing_extensions.NotRequired[str]
    """
    Assessor's Parcel Number
    """

    city: typing_extensions.NotRequired[str]
    """
    City name
    """

    fips: typing_extensions.NotRequired[str]
    """
    FIPS county code
    """

    key: typing_extensions.NotRequired[str]
    """
    User-provided key for matching request to response
    """

    state: typing_extensions.NotRequired[str]
    """
    Two-letter state code
    """

    street: typing_extensions.NotRequired[str]
    """
    Street address
    """

    zip: typing_extensions.NotRequired[str]
    """
    5-digit ZIP code
    """


class _SerializerAddressToVerify(pydantic.BaseModel):
    """
    Serializer for AddressToVerify handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    address: typing.Optional[str] = pydantic.Field(alias="address", default=None)
    apn: typing.Optional[str] = pydantic.Field(alias="apn", default=None)
    city: typing.Optional[str] = pydantic.Field(alias="city", default=None)
    fips: typing.Optional[str] = pydantic.Field(alias="fips", default=None)
    key: typing.Optional[str] = pydantic.Field(alias="key", default=None)
    state: typing.Optional[str] = pydantic.Field(alias="state", default=None)
    street: typing.Optional[str] = pydantic.Field(alias="street", default=None)
    zip: typing.Optional[str] = pydantic.Field(alias="zip", default=None)
