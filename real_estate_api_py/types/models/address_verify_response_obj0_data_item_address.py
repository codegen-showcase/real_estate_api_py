import pydantic
import typing


class AddressVerifyResponseObj0DataItemAddress(pydantic.BaseModel):
    """
    AddressVerifyResponseObj0DataItemAddress
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    address: typing.Optional[str] = pydantic.Field(alias="address", default=None)
    carrier_route: typing.Optional[str] = pydantic.Field(
        alias="carrierRoute", default=None
    )
    city: typing.Optional[str] = pydantic.Field(alias="city", default=None)
    congressional_district: typing.Optional[str] = pydantic.Field(
        alias="congressionalDistrict", default=None
    )
    county: typing.Optional[str] = pydantic.Field(alias="county", default=None)
    fips: typing.Optional[str] = pydantic.Field(alias="fips", default=None)
    house: typing.Optional[str] = pydantic.Field(alias="house", default=None)
    label: typing.Optional[str] = pydantic.Field(alias="label", default=None)
    pre_direction: typing.Optional[str] = pydantic.Field(
        alias="preDirection", default=None
    )
    state: typing.Optional[str] = pydantic.Field(alias="state", default=None)
    street: typing.Optional[str] = pydantic.Field(alias="street", default=None)
    street_type: typing.Optional[str] = pydantic.Field(alias="streetType", default=None)
    zip: typing.Optional[str] = pydantic.Field(alias="zip", default=None)
    zip4: typing.Optional[str] = pydantic.Field(alias="zip4", default=None)
