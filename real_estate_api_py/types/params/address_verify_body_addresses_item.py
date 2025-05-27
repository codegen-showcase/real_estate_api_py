import pydantic
import typing
import typing_extensions


class AddressVerifyBodyAddressesItem(typing_extensions.TypedDict):
    """
    AddressVerifyBodyAddressesItem
    """

    address: typing_extensions.NotRequired[str]
    """
    Formatted address including street, city, state and zip.
    """

    apn: typing_extensions.NotRequired[str]

    city: typing_extensions.NotRequired[str]
    """
    Name of the city where the address is located.
    """

    fips: typing_extensions.NotRequired[str]

    key: typing_extensions.NotRequired[str]
    """
    This key will be returned in the response per address submitted to help relate the request to the response data.
    """

    state: typing_extensions.NotRequired[str]
    """
    Two letter abbreviation for the state where the address is located.
    """

    street: typing_extensions.NotRequired[str]
    """
    Contains the house number, pre-direction, street name, street type and post-direction.
    """

    zip: typing_extensions.NotRequired[str]
    """
    Five digit zip code where the property is located.
    """


class _SerializerAddressVerifyBodyAddressesItem(pydantic.BaseModel):
    """
    Serializer for AddressVerifyBodyAddressesItem handling case conversions
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
