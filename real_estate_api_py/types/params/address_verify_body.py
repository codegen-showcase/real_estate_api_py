import pydantic
import typing
import typing_extensions

from .address_verify_body_addresses_item import (
    AddressVerifyBodyAddressesItem,
    _SerializerAddressVerifyBodyAddressesItem,
)


class AddressVerifyBody(typing_extensions.TypedDict):
    """
    AddressVerifyBody
    """

    addresses: typing_extensions.NotRequired[
        typing.List[AddressVerifyBodyAddressesItem]
    ]
    """
    Provide up to 100 addresses per request
    """

    strict: typing_extensions.NotRequired[bool]


class _SerializerAddressVerifyBody(pydantic.BaseModel):
    """
    Serializer for AddressVerifyBody handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    addresses: typing.Optional[
        typing.List[_SerializerAddressVerifyBodyAddressesItem]
    ] = pydantic.Field(alias="addresses", default=None)
    strict: typing.Optional[bool] = pydantic.Field(alias="strict", default=None)
